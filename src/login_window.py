import time
import hashlib

from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import util
import config

from log import Logger


class Form(QDialog):

    def __init__(self, console, parent=None):
        super(Form, self).__init__(parent)
        self.console = console

        self.logger = Logger('Login', console.log_level)

        self.setWindowTitle("PttOTP 登入視窗")

        self.setMinimumWidth(260)
        self.setMinimumHeight(150)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(util.load_icon(config.icon_small)))
        # Create widgets

        layout = QVBoxLayout()

        label = QLabel()
        pixmap = util.load_icon(config.icon_small)
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)

        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(QLabel())

        label = QLabel('批踢踢帳號')
        label.setFont(config.font)
        label.setAlignment(Qt.AlignCenter)
        self.label_id = label

        # self.label_id = QLabel('批踢踢帳號')
        # self.label_id.setAlignment(Qt.AlignCenter)
        self.edit_id = QLineEdit()
        self.edit_id.setMaximumWidth(150)
        self.edit_id.setAlignment(Qt.AlignHCenter)
        layout_id = QHBoxLayout()
        layout_id.addWidget(self.edit_id)

        label = QLabel('批踢踢密碼')
        label.setAlignment(Qt.AlignCenter)
        label.setFont(config.font)
        self.label_pw = label

        edit = QLineEdit()
        edit.setAlignment(Qt.AlignHCenter)
        edit.setEchoMode(QLineEdit.Password)
        edit.setFont(config.font)
        edit.setMaximumWidth(150)
        layout_pw = QHBoxLayout()
        layout_pw.addWidget(edit)
        self.edit_pw = edit

        self.button = QPushButton("登入")
        self.button.setMaximumWidth(80)
        self.button.clicked.connect(self.login)
        layout_b = QHBoxLayout()
        layout_b.addWidget(self.button)

        layout.addWidget(self.label_id)
        layout.addLayout(layout_id)
        layout.addWidget(self.label_pw)
        layout.addLayout(layout_pw)
        layout.addLayout(layout_b)
        layout.addWidget(QLabel())
        layout.addWidget(QLabel(f'版本: {config.version}'))
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot

        self.ptt_adapter = None
        self.next = False

    def wait_login(self, ptt_id, ptt_pw):

        self.ptt_adapter.login(ptt_id, ptt_pw)
        while not self.ptt_adapter.login_finish:
            time.sleep(0.5)


    def login(self):

        ptt_id = self.edit_id.text()
        ptt_pw = self.edit_pw.text()

        if len(ptt_id) <= 2 or len(ptt_pw) <= 3:
            return

        self.logger.show(Logger.INFO, '開始登入')

        self.ptt_adapter = self.console.ptt_adapter

        self.wait_login(ptt_id, ptt_pw)

        if not self.ptt_adapter.login_success:
            self.edit_id.setText('')
            self.edit_pw.setText('')
            return

        self.logger.show(Logger.INFO, '登入成功')
        self.next = True
        self.console.ptt_id = ptt_id

        self.console.config.load()

        hash_value = hashlib.sha256(ptt_pw.encode('utf-8')).hexdigest()
        self.console.config.set(config.key_hash_pw, hash_value)
        self.console.config.write()

        self.close()

    def closeEvent(self, event):
        if not self.next:
            self.logger.show(Logger.INFO, '直接關閉')
            self.console.system_alert('背景執行中')
