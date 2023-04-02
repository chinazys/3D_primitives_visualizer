import sys

from PyQt5.QtWidgets import (QApplication)

from ui.app_window import AppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myApp = AppWindow(app)
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')