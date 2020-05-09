import sys
import time
from PySide2.QtWidgets import QApplication
import ptt_adapter

import console
import login_window

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form

    console = console.Console()
    console.ptt_adapter = ptt_adapter.API()

    login_window = login_window.Form(console)
    login_window.show()
    login_window.exec_()
    # Run the main Qt loop
    if login_window.next:
        print('next')
    else:
        print('close sys')

    # app.exec_()
    sys.exit()
