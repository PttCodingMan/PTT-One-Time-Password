import sys

from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton, QApplication, QVBoxLayout, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

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

        self.logger = Logger('Rule', console.log_level)

        self.setWindowTitle("PttOTP 使用守則")

        self.setMinimumWidth(250)
        self.setWindowIcon(QIcon(util.load_icon(config.icon_small)))

        rule_text = '''
以下為 Ptt OTP 使用守則，如不同意或無法遵守
請勿使用本軟體

1. 註冊批踢踢動態密碼後，會產生帳號專屬檔案在 data 資料夾，內含所有批踢踢動態密碼相關重要資訊，建議備份此資料夾，以保護您動態密碼金鑰的安全
一旦遺失所有備份或者硬碟毀損，作者也無法將您的帳號密碼恢復，請使用信箱重設密碼功能，以恢復您的帳號密碼
2. 如果您的批踢踢動態密碼程式，不幸因為各種原因當機或者關閉，您可以直接重啟程式，批踢踢動態密碼會自動恢復您的動態密碼功能
3. 批踢踢動態密碼，會顯示並儲存敏感資訊，請勿在公共電腦上執行批踢踢動態密碼
4. 切勿同時執行兩個以上批踢踢動態密碼程式
5. 免責聲明，軟體皆存在無法迴避之風險，經使用本軟體造成所有損害皆與開發者無關
'''
        rule_text = rule_text.strip()

        layout = QVBoxLayout()
        for rule_line in rule_text.split('\n'):
            label = QLabel(rule_line)
            label.setFont(config.font)
            layout.addWidget(label)
        # Set dialog layout

        button_layout = QHBoxLayout()

        ok_button = QPushButton("我同意並會遵守")
        ok_button.clicked.connect(self.click_ok)
        button_layout.addWidget(ok_button)

        not_ok_button = QPushButton("恕我無法同意並遵守")
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
