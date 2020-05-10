import sys
import threading
import time
from PyPtt import PTT
import util

from log import Logger


class API:
    def __init__(self, console):

        self.console = console
        self.logger = Logger('PTT', Logger.INFO)

        self.reset()

    def reset(self):

        self.login_success = False
        self.call_logout = False
        self.login_finish = True

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

    def run(self):
        ptt_bot = PTT.API()

        self.login_finish = False
        try:
            ptt_bot.login(
                self.ptt_id,
                self.ptt_pw,
                kick_other_login=True
            )
        except PTT.exceptions.LoginError:
            ptt_bot.log('登入失敗')
            self.console.system_alert('登入失敗')
            self.login_finish = True
            return
        except PTT.exceptions.WrongIDorPassword:
            ptt_bot.log('帳號密碼錯誤')
            self.console.system_alert('帳號密碼錯誤')
            self.login_finish = True
            return
        except PTT.exceptions.LoginTooOften:
            ptt_bot.log('請稍等一下再登入')
            self.console.system_alert('請稍等一下再登入')
            self.login_finish = True
            return

        self.login_finish = True
        self.console.ptt_id = self.ptt_id

        self.login_success = True

        while not self.call_logout:
            time.sleep(0.1)

        ptt_bot.logout()

        self.reset()
