import sys
from PySide2.QtWidgets import (QLabel, QHBoxLayout, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

from PySide2.QtCore import Qt
import util
import config
from log import Logger


class Form(QDialog):

    def __init__(self, console, parent=None):
        super(Form, self).__init__(parent)
        flag = self.windowFlags()
        flag &= ~Qt.WindowCloseButtonHint
        flag |= Qt.WindowStaysOnTopHint
        self.setWindowFlags(flag)
        self.console = console

        self.logger = Logger('Rule', Logger.INFO)

        self.setWindowTitle("PttOTP 使用守則")

        self.setMinimumWidth(250)
        self.setWindowIcon(util.load_icon(config.icon_small))

        rule_text = '''
以下為 Ptt OTP 使用守則，如不同意或無法遵守
請勿使用本軟體

1. 切勿同一帳號同時執行兩個以上批踢踢動態密碼程式
2. Ptt OTP 會顯示並儲存敏感資訊，請勿在公共電腦上執行
3. 軟體出錯難免，如軟體無法正確還原您的密碼，請使用註冊
    信箱取回帳號功能
'''
        rule_text = rule_text.strip()

        layout = QVBoxLayout()
        for rule_line in rule_text.split('\n'):
            layout.addWidget(QLabel(rule_line))
        # Set dialog layout

        button_layout = QHBoxLayout()

        ok_button = QPushButton("我會遵守")
        ok_button.clicked.connect(self.click_ok)
        button_layout.addWidget(ok_button)

        not_ok_button = QPushButton("無法遵守")
        not_ok_button.clicked.connect(self.click_not_ok)
        button_layout.addWidget(not_ok_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.ok = False

    def click_ok(self):
        self.logger.show(Logger.INFO, '我會遵守')
        self.ok = True
        self.close()

    def click_not_ok(self):
        self.logger.show(Logger.INFO, '無法遵守')
        self.ok = False
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    form = Form(None)
    form.exec_()

    if form.ok:
        print('click ok')
    else:
        print('click not ok')

    sys.exit()
