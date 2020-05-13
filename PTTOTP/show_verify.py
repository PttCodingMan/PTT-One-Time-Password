
import sys
import pyotp
from PySide2.QtWidgets import (QLabel, QHBoxLayout, QPushButton, QApplication,
                               QVBoxLayout, QDialog, QLineEdit)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
import util
import config
from log import Logger


class Form(QDialog):
    def __init__(self, console, otp_key, parent=None):
        super(Form, self).__init__(parent)
        self.console = console
        self.otp_key = otp_key

        self.logger = Logger('Rule', Logger.INFO)

        self.setWindowTitle("PttOTP 驗證視窗")
        self.setWindowIcon(util.load_icon(config.icon_small))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        rule_text = '''
1. 請開啟 google authenticator 掃描以下圖片
2. 於下方輸入框輸入 google authenticator 顯示的驗證碼
'''
        rule_text = rule_text.strip()

        layout = QVBoxLayout()
        for rule_line in rule_text.split('\n'):
            layout.addWidget(QLabel(rule_line))

        label = QLabel()
        label.setPixmap(QPixmap('./temp.png'))
        layout.addWidget(label)

        button_layout = QHBoxLayout()

        self.otp_edit = QLineEdit()
        button_layout.addWidget(self.otp_edit)

        ok_button = QPushButton("驗證")
        ok_button.clicked.connect(self.click_verify)
        button_layout.addWidget(ok_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.ok = False

    def click_verify(self):
        self.logger.show(Logger.INFO, '驗證')

        current_otp = self.otp_edit.text()
        self.logger.show_value(Logger.INFO, 'Current otp', current_otp)

        otp_obj = pyotp.TOTP(self.otp_key)
        otp = otp_obj.now()

        self.logger.show_value(Logger.INFO, 'otp', otp)

        if current_otp != otp:
            self.console.system_alert('驗證失敗請再輸入一次')
            return

        self.ok = True
        self.close()
        self.console.system_alert('驗證成功')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    pixmap = QPixmap('./test.png')
    form = Form(None, pixmap)
    form.exec_()

    if form.ok:
        print('click ok')
    else:
        print('click not ok')

    sys.exit()
