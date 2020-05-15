import sys
from PySide2.QtWidgets import QApplication
import ptt_adapter

from log import Logger
import console
import systemtray
import config

if __name__ == '__main__':

    logger = Logger('OTP', Logger.INFO)

    logger.show_value(Logger.INFO, '版本', config.version)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    console = console.Console()
    if console.test_mode:
        logger.show(Logger.INFO, '測試模式')
    console.config = config.Config(console)
    console.ptt_adapter = ptt_adapter.API(console)


    system_tray = systemtray.Form(console)
    app.exec_()
    sys.exit()
