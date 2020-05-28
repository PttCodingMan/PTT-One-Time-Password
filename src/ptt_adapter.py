import threading
import time
import pyotp
from PyPtt import PTT

from log import Logger
import config


class API:
    def __init__(self, console):

        self.console = console
        self.logger = Logger('PTT', Logger.INFO)

        self.reset()

    def reset(self):

        self.login_success = False
        self.call_logout = False
        self.login_finish = True
        self.otp = None
        self.catch_error = False
        self.first = True

        self.logger.show(Logger.INFO, '重設資料完成')

    def logout(self):

        self.logger.show(Logger.INFO, '開始登出')

        if self.login_success:
            self.call_logout = True

            while self.call_logout:
                time.sleep(0.5)

        self.logger.show(Logger.INFO, '登出完成')

    def login(self, ptt_id, ptt_pw):

        self.ptt_id = ptt_id
        self.ptt_pw = ptt_pw

        self.login_success = False
        self.call_logout = False

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )
        self.thread.start()
        time.sleep(0.1)

    def enable_otp(self):

        otp_key = self.console.config.get(config.key_otp_key)
        self.otp = pyotp.TOTP(otp_key)

    def run(self):

        if self.console.test_local:
            ptt_bot = PTT.API(
                host=PTT.data_type.host_type.LOCALHOST,
                connect_mode=PTT.connect_core.connect_mode.TELNET,
                port=8888
            )
        else:
            ptt_bot = PTT.API()

        while True:

            if self.console.test_mode:
                current_pw = self.ptt_pw
            else:
                if self.catch_error:
                    current_pw = last_otp
                else:
                    current_pw = self.ptt_pw

            self.login_finish = False
            recover_level = 0
            kick_other_login = False
            while True:
                try:

                    if self.call_logout:
                        break
                    ptt_bot.login(
                        self.ptt_id,
                        current_pw,
                        kick_other_login=kick_other_login
                    )
                except PTT.exceptions.WrongIDorPassword:
                    ptt_bot.log('帳號密碼錯誤')
                    self.console.ptt_id = self.ptt_id
                    if not self.console.config.loaded:
                        self.console.config.load()

                    if recover_level >= 2:
                        self.console.system_alert('無法恢復')
                        self.login_finish = True
                        return
                    elif self.console.config.get(config.key_running):

                        kick_other_login = True
                        if recover_level == 0:
                            recover_level += 1
                            self.console.system_alert('從錯誤恢復中')

                            current_pw = self.console.config.get(config.key_current_otp)
                            self.logger.show_value(Logger.INFO, '恢復最後密碼', current_pw)
                        elif recover_level == 1:
                            recover_level += 1

                            current_pw = self.console.config.get(config.key_last_otp)
                            self.logger.show_value(Logger.INFO, '恢復最後密碼', current_pw)
                        continue
                    else:
                        self.console.system_alert('帳號密碼錯誤')
                        self.login_finish = True
                        return
                except PTT.exceptions.LoginError:
                    ptt_bot.log('登入失敗')
                    self.console.system_alert('登入失敗')
                    self.login_finish = True
                    return
                except PTT.exceptions.LoginTooOften:
                    ptt_bot.log('請稍等一下再登入')
                    self.console.system_alert('請稍等一下再登入')
                    self.login_finish = True
                    return
                except PTT.exceptions.ConnectError:
                    self.console.system_alert('連線有問題')
                    if self.catch_error:
                        continue
                    else:
                        self.login_finish = True
                        return
                break

            if recover_level != 0:
                self.console.system_alert('從錯誤恢復成功')

            self.catch_error = False
            self.login_finish = True
            self.console.ptt_id = self.ptt_id

            self.login_success = True

            last_otp = ''
            while not self.call_logout:
                time.sleep(0.1)
                if self.otp is not None:
                    current_otp = self.otp.now()

                    if last_otp != current_otp:
                        self.logger.show_value(Logger.INFO, '新密碼', current_otp)

                        self.console.config.set(config.key_current_otp, current_otp)
                        self.console.config.set(config.key_last_otp, last_otp)
                        self.console.config.write()

                        try:
                            if self.console.test_mode:
                                ptt_bot.change_pw(self.ptt_pw)
                            else:
                                ptt_bot.change_pw(current_otp)
                        except PTT.exceptions.ConnectionClosed:
                            self.catch_error = True
                            break
                        except PTT.exceptions.Timeout:
                            self.catch_error = True
                            break

                        self.console.current_otp = current_otp
                        if self.console.otp_form is not None:
                            self.console.otp_form.update_otp()
                        last_otp = current_otp
                        self.logger.show(Logger.INFO, '密碼變更完成')

            if self.catch_error:
                continue

            if self.otp is not None:
                ptt_bot.change_pw(self.ptt_pw)
            break

        ptt_bot.logout()

        self.reset()
