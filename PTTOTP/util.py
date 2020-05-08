import sys

from PySide2.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)
from PySide2.QtWidgets import QMessageBox


def get_bytes_from_file(filename):
    return open(filename, "rb").read().hex()


def hex_byte(hex):
    return bytearray.fromhex(hex)


def alert(msg_str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText(msg_str)
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle("PttOTP")
    # msg.setDetailedText("The details are as follows:")
    # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setStandardButtons(QMessageBox.Ok)
    # msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()


if __name__ == '__main__':
    # hex = get_bytes_from_file('../PTTOTP_small.png')
    # print(hex)

    app = QApplication(sys.argv)
    alert()

    sys.exit()