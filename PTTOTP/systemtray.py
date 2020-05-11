import sys
import os
import time
import pyotp
import qrcode
from PySide2.QtWidgets import QSystemTrayIcon
from PySide2.QtWidgets import QMenu
import util
import config
from log import Logger
import login_window
import rule_window
import show_verify
import about_window


class Form(QSystemTrayIcon):
    def __init__(self, console):
        super(Form, self).__init__(None)

        self.logger = Logger('OTP', Logger.INFO)

        self.console = console
        console.system_alert = self.system_alert

        self.icon = util.load_icon(config.icon_small)
        self.setIcon(self.icon)

        self.set_menu(False)

        self.setToolTip('Ptt OTP')

        self.show()

        self.activated.connect(self.icon_clicked)

        self.login_success = False

        self.show_login_form()

    def set_menu(self, is_login):

        menu = QMenu()

        if is_login:
            self.logger.show_value(Logger.INFO, '設定選單', '登出')
            act = menu.addAction("登出")
            act.triggered.connect(self.logout)
        else:
            self.logger.show_value(Logger.INFO, '設定選單', '登入')
            act = menu.addAction("登入")
            act.triggered.connect(self.show_login_form)

        act = menu.addAction("關於")
        act.triggered.connect(self.aoubt_func)
        menu.addSeparator()
        act = menu.addAction("離開")
        act.triggered.connect(self.exit_func)

        self.setContextMenu(menu)

    def aoubt_func(self):
        self.logger.show(Logger.INFO, '啟動關於視窗')
        about_window_form = about_window.Form(self.console)
        about_window_form.exec_()

    def logout(self):
        self.login_success = False
        self.set_menu(False)
        self.console.ptt_adapter.logout()

    def show_login_form(self):
        login_form = login_window.Form(self.console)
        login_form.show()
        login_form.exec_()

        if not login_form.next:
            return

        self.login_success = True

        self.set_menu(True)

        if not os.path.exists('./data'):
            os.makedirs('./data')

        current_path = f'./data/{self.console.ptt_id}'
        if not os.path.exists(current_path):
            os.makedirs(current_path)

        self.console.config.load()
        if self.console.config.get(config.key_otp_key) is None:

            self.system_alert(f'{self.console.ptt_id} 歡迎使用 Ptt OTP')
            rule_form = rule_window.Form(self.console)
            rule_form.show()
            rule_form.exec_()

            if not rule_form.ok:
                self.system_alert('Ptt OTP 感謝您的試用')
                time.sleep(3)
                self.exit_func()

            otp_key = pyotp.random_base32()

            otp_url = pyotp.totp.TOTP(otp_key).provisioning_uri(self.console.ptt_id, issuer_name="Ptt OTP")
            img = qrcode.make(otp_url)
            img.save('./temp.png')

            show_verify_form = show_verify.Form(self.console, otp_key)
            show_verify_form.show()
            show_verify_form.exec_()

            os.remove('./temp.png')

            if not show_verify_form.ok:
                self.system_alert('Ptt OTP 感謝您的試用')
                time.sleep(3)
                self.exit_func()

            self.console.config.set(config.key_otp_key, otp_key)

        else:
            self.system_alert(f'{self.console.ptt_id} 歡迎回來')

        otp_key = self.console.config.get(config.key_otp_key)
        # print(otp_key)
        # print(self.console.ptt_id)

    def system_alert(self, msg):
        self.showMessage('Ptt OTP', msg, self.icon)

    def icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.logger.show(Logger.INFO, 'DoubleClick')
            if not self.login_success:
                self.show_login_form()

    def exit_func(self):
        self.logger.show(Logger.DEBUG, '離開')
        self.logout()
        sys.exit()
