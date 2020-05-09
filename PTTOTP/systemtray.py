import sys

from PySide2.QtWidgets import QSystemTrayIcon
from PySide2.QtWidgets import QMenu
import util
import config

from log import Logger
import login_window


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

        self.system_alert('Ptt OTP 啟動')

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
