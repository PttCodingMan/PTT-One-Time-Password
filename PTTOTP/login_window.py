import sys
import time

from PySide2.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QByteArray

import util
import config

from log import Logger
class Form(QDialog):

    def __init__(self, console, parent=None):
        super(Form, self).__init__(parent)
        self.console = console

        self.logger = Logger('Login', Logger.INFO)

        self.setWindowTitle("PttOTP 登入視窗")

        self.setMinimumWidth(250)

        self.setWindowIcon(util.load_icon(config.icon_small))
        # Create widgets
        self.label_id = QLabel('請輸入批踢踢帳號')
        self.edit_id = QLineEdit()
        self.label_pw = QLabel('請輸入批踢踢密碼')
        self.edit_pw = QLineEdit()
        self.edit_pw.setEchoMode(QLineEdit.Password)
        self.button = QPushButton("登入")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_id)
        layout.addWidget(self.edit_id)
        layout.addWidget(self.label_pw)
        layout.addWidget(self.edit_pw)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.login)

        self.ptt_adapter = None
        self.next = False

    # Greets the user
    def login(self):

        self.logger.show(Logger.INFO, '開始登入')

        ptt_id = self.edit_id.text()
        ptt_pw = self.edit_pw.text()

        self.ptt_adapter = self.console.ptt_adapter

        self.ptt_adapter.login(ptt_id, ptt_pw)
        while not self.ptt_adapter.login_success:
            time.sleep(0.5)

        self.logger.show(Logger.INFO, '開始成功')
        self.next = True

        self.close()

    # def closeEvent(self, event):
    #     print('close')
    #     if self.ptt_adapter is not None:
    #         self.ptt_adapter.logout()
    #
    #     event.accept()

