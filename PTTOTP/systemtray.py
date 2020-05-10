import sys
import os
import time
import pyotp
from PySide2.QtWidgets import QSystemTrayIcon
from PySide2.QtWidgets import QMenu
import util
import config
from log import Logger
import login_window
import rule_window


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

        self.login_form = login_window.Form(console)
        self.show_login_form()

    def set_menu(self, is_login):

        menu = QMenu()

        if is_login:
            act = menu.addAction("登出")
            act.triggered.connect(self.logout)
        else:
            act = menu.addAction("登入")
            act.triggered.connect(self.show_login_form)

        menu.addSeparator()
        act = menu.addAction("離開")
        act.triggered.connect(self.exit_func)

        self.setContextMenu(menu)

    def logout(self):
        self.set_menu(False)
        self.console.ptt_adapter.logout()

    def show_login_form(self):
        self.login_form.show()
        self.login_form.exec_()

        if not self.login_form.next:
            self.set_menu(False)
            return

        self.set_menu(True)

        if not os.path.isdir('./data'):
            os.makedirs('./data')

        current_path = f'./data/{self.login_form.ptt_id}'
        if not os.path.isdir(current_path):

            self.system_alert(f'{self.login_form.ptt_id} 歡迎使用 Ptt OTP')
            rule_form = rule_window.Form(self.console)
            rule_form.show()
            rule_form.exec_()

            if not rule_form.ok:
                self.system_alert('Ptt OTP 感謝您的試用')
                time.sleep(5)
                self.exit_func()

            os.makedirs(current_path)
            otp_key = pyotp.random_base32()
            self.console.config.set(config.key_otp_key, otp_key)
        else:
            self.system_alert(f'{self.login_form.ptt_id} 歡迎回來')

        print(self.login_form.ptt_id)


    def system_alert(self, msg):
        self.showMessage('Ptt OTP', msg, self.icon)

    def icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_login_form()

    def double_click(self):
        self.logger.show(Logger.DEBUG, '雙點擊')

    def exit_func(self):
        self.logger.show(Logger.DEBUG, '離開')
        self.logout()
        sys.exit()
