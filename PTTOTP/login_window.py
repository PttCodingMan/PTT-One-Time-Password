import sys
import time

from PySide2.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QByteArray

import util
import config


class Form(QDialog):

    def __init__(self, console, parent=None):
        super(Form, self).__init__(parent)
        self.console = console
        self.setWindowTitle("PttOTP 登入視窗")

        self.setMinimumWidth(250)
        qbyte = QByteArray(util.hex_byte(config.icon_small))

        qicon = QPixmap()
        qicon.loadFromData(qbyte, "png")

        self.setWindowIcon(qicon)
        # Create widgets
        self.label_id = QLabel('請輸入批踢踢帳號')
        self.edit_id = QLineEdit()
        self.label_pw = QLabel('請輸入批踢踢密碼')
        self.edit_pw = QLineEdit()
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
        self.button.clicked.connect(self.greetings)

        self.ptt_adapter = None
        self.next = False

    # Greets the user
    def greetings(self):
        print("Hello %s" % self.edit_id.text())
        print("Hello %s" % self.edit_pw.text())

        ptt_id = self.edit_id.text()
        ptt_pw = self.edit_pw.text()

        self.ptt_adapter = self.console.ptt_adapter

        self.ptt_adapter.login(ptt_id, ptt_pw)
        while not self.ptt_adapter.login_success:
            time.sleep(0.5)

        print('login success')
        self.next = True

        self.close()

    # def closeEvent(self, event):
    #     print('close')
    #     if self.ptt_adapter is not None:
    #         self.ptt_adapter.logout()
    #
    #     event.accept()

