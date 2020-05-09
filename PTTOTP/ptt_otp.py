import sys
from PySide2.QtWidgets import QApplication
import ptt_adapter

from log import Logger
import console
import systemtray

version = '0.1.0'

if __name__ == '__main__':

    logger = Logger('OTP', Logger.INFO)

    logger.show_value(Logger.INFO, '版本', version)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    console = console.Console()
    console.ptt_adapter = ptt_adapter.API(console)

    system_tray = systemtray.Form(console)
    app.exec_()
    sys.exit()