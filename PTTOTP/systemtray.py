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

        menu = QMenu()

        exit_act = menu.addAction("離開")
        exit_act.triggered.connect(self.exit_func)

        self.setContextMenu(menu)
        self.setToolTip('Ptt OTP')

        self.show()

        self.activated.connect(self.icon_clicked)

        self.login_form = login_window.Form(console)
        self.show_login_form()

        self.system_alert('Ptt OTP 啟動')

    def show_login_form(self):
        self.login_form.show()

    def system_alert(self, msg):
        self.showMessage('Ptt OTP', msg, self.icon)

    def icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_login_form()

    def double_click(self):
        self.logger.show(Logger.DEBUG, '雙點擊')

    def exit_func(self):
        self.logger.show(Logger.DEBUG, '離開')
        self.console.ptt_adapter.logout()
        sys.exit()
