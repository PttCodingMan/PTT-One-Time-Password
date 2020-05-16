import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMessageBox

from PySide2.QtGui import QPixmap
from PySide2.QtCore import QByteArray


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


def load_icon(icon_string):
    q_byte = QByteArray(hex_byte(icon_string))
    q_icon = QPixmap()
    q_icon.loadFromData(q_byte, "png")
    return q_icon


if __name__ == '__main__':
    # hex = get_bytes_from_file('../PTTOTP_small.png')
    # print(hex)

    app = QApplication(sys.argv)
    alert()

    sys.exit()
