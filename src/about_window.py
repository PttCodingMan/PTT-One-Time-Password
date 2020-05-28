import sys
import os
from PySide2.QtWidgets import (QLabel, QApplication,
                               QVBoxLayout, QDialog)

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

import util
import config
from log import Logger


class Form(QDialog):

    def __init__(self, console, parent=None):
        super(Form, self).__init__(parent)
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.console = console

        self.logger = Logger('About', console.log_level)

        self.setWindowTitle("關於 Ptt OTP")

        self.setWindowIcon(util.load_icon(config.icon_small))

        layout = QVBoxLayout()

        label = QLabel()

        pixmap = util.load_icon(config.icon_small)
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)

        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        label = QLabel()
        layout.addWidget(label)

        rule_text = '''
這是一個希望可以守護 PTT 使用者的專案

'''
        rule_text = rule_text.strip()

        for rule_line in rule_text.split('\n'):
            label = QLabel(rule_line)
            label.setFont(config.font)
            layout.addWidget(label)

        label = QLabel()
        label.setFont(config.font)
        label.setOpenExternalLinks(True)
        label.setText(
            f'Ptt One Time Password v {config.version}')
        # label.setMinimumHeight(MinimumHeight)
        layout.addWidget(label)

        label = QLabel()
        label.setFont(config.font)
        label.setOpenExternalLinks(True)
        label.setText(
            '專案網址: <a href=\"https://git.io/Jf0s7\">PTT-One-Time-Password</a>')
        # label.setMinimumHeight(MinimumHeight)
        layout.addWidget(label)

        label = QLabel()
        label.setFont(config.font)
        label.setOpenExternalLinks(True)
        label.setText(
            '開發者: <a href=\"https://pttcodingman.github.io/\">CodingMan</a>')
        # label.setMinimumHeight(MinimumHeight)
        layout.addWidget(label)

        self.setLayout(layout)

        self.setFixedSize(241, 330)
        self.click_count = 0

    def mouseDoubleClickEvent(self, event):
        # print(self.width())
        # print(self.height())
        self.click_count += 1
        if self.click_count == 2 or self.click_count == 3:
            self.console.system_alert("別戳了")

        if self.click_count == 4:
            self.console.system_alert("就跟你說別戳了")

        if self.click_count == 5:
            self.console.system_alert("我很認真地跟你說別戳了")

        if self.click_count == 6:
            self.console.system_alert("會痛啦 乾")

        if self.click_count == 7:
            self.console.system_alert("欸 現在是不是逼我翻臉")

        if self.click_count == 8:
            self.console.system_alert("幹 你真的很北爛")

        if self.click_count == 9:
            self.console.system_alert("我要搬救兵了")

        if self.click_count >= 10:
            self.console.system_alert("有種你就戳他!!")
            os.system("start \"\" https://www.facebook.com/CodingPlace/")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    form = Form(None)
    form.exec_()

    # if form.ok:
    #     print('click ok')
    # else:
    #     print('click not ok')

    sys.exit()
