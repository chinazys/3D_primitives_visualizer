from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction

class MenuBar:
    def __init__(self, window, app):
        self.menu = window.menuBar()

        self.menu_file = self.menu.addMenu("File")
        exit = QAction("Exit", window, triggered=app.quit)
        self.menu_file.addAction(exit)

        self.menu_about = self.menu.addMenu("&About")
        about = QAction("About Qt", window, shortcut=QKeySequence(QKeySequence.StandardKey.HelpContents),
                        triggered=app.aboutQt)
        self.menu_about.addAction(about)