import sys
import threading
import time
from PyPtt import PTT
import util


class API:
    def __init__(self, ptt_id, ptt_pw):

        self.ptt_id = ptt_id
        self.ptt_pw = ptt_pw

        self.login_success = False
        self.call_logout = False

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )
        self.thread.start()
        time.sleep(0.5)

    def logout(self):
        self.call_logout = True

    def run(self):
        ptt_bot = PTT.API()

        try:
            ptt_bot.login(
                self.ptt_id,
                self.ptt_pw,
                kick_other_login=True
            )
        except PTT.exceptions.LoginError:
            ptt_bot.log('登入失敗')
            util.alert('登入失敗')
            sys.exit()
        except PTT.exceptions.WrongIDorPassword:
            ptt_bot.log('帳號密碼錯誤')
            util.alert('帳號密碼錯誤')
            sys.exit()
        except PTT.exceptions.LoginTooOften:
            ptt_bot.log('請稍等一下再登入')
            util.alert('請稍等一下再登入')
            sys.exit()

        self.login_success = True

        while not self.call_logout:
            time.sleep(0.1)

        ptt_bot.logout()
        self.login_success = False
