import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QByteArray


def get_bytes_from_file(filename):
    return open(filename, "rb").read().hex()


def hex_byte(hex):
    return bytearray.fromhex(hex)

def load_icon(icon_string):
    q_byte = QByteArray(hex_byte(icon_string))
    q_icon = QPixmap()
    q_icon.loadFromData(q_byte, "png")
    return q_icon


if __name__ == '__main__':
    pass
    # hex = get_bytes_from_file('../PTTOTP_small.png')
    # print(hex)
