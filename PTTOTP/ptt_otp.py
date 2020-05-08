import sys
import time
from PySide2.QtWidgets import QApplication

import login_window

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = login_window.Form()
    form.show()
    # Run the main Qt loop

    sys.exit(app.exec_())
