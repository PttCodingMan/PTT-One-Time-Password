import sys
from PySide2.QtWidgets import (QLabel, QHBoxLayout, QPushButton, QApplication,
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

        self.logger = Logger('About', Logger.INFO)

        self.setWindowTitle("關於 Ptt OTP")

        self.setWindowIcon(util.load_icon(config.icon_small))

        layout = QVBoxLayout()

        label = QLabel()

        pixmap = util.load_icon(config.person_logo)
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)

        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

#         rule_text = '''
# 開發者: CodingMan
# 專案網址: https://github.com/PttCodingMan/PTT-One-Time-Password
# '''
#         rule_text = rule_text.strip()

        # for rule_line in rule_text.split('\n'):
        #     label = QLabel(rule_line)
        #     label.setOpenExternalLinks(True)
        #     # label.setText("<a href=\"http://www.qtcentre.org\">QtCentre</a>");
        #     layout.addWidget(label)

        label = QLabel()
        layout.addWidget(label)

        label = QLabel()
        label.setOpenExternalLinks(True)
        label.setText(
            f'Ptt One Time Password v {config.version}')
        label.setMinimumHeight(20)
        layout.addWidget(label)

        label = QLabel()
        label.setOpenExternalLinks(True)
        label.setText(
            '開發者: <a href=\"https://pttcodingman.github.io/\">CodingMan</a>')
        label.setMinimumHeight(20)
        layout.addWidget(label)

        label = QLabel()
        label.setOpenExternalLinks(True)
        label.setText('專案網址: <a href=\"https://github.com/PttCodingMan/PTT-One-Time-Password\">https://github.com/PttCodingMan/PTT-One-Time-Password</a>')
        label.setMinimumHeight(20)
        layout.addWidget(label)

        self.setLayout(layout)


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
