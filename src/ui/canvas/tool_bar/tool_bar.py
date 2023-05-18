from PyQt5.QtWidgets import (QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from os import getcwd

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from ui.help_panel.help_panel import HelpPanel

class ToolBar:
    def __init__(self, canvas, window):
        self.window = window

        self.help_is_shown = False

        self.help_panel = HelpPanel(self.window)

        self.button_help = QPushButton()
        self.button_help.setFixedWidth(45)
        self.button_help.setFixedHeight(45)
        self.button_help.setStyleSheet("QPushButton { background-color: transparent; margin: 0px; padding: 0px; border: 0px } QPushButton:hover {background-color: rgb(229,243,255); margin 0px; padding: 0px; border: 2px solid #cee9ff; border-radius: 4px;}")
        self.button_help.setIcon(QIcon(getcwd() + "/icons/help.png"))
        self.button_help.setIconSize(QSize(35, 35))
        self.button_help.clicked.connect(self.help_button_click)

        self.toolbar = NavigationToolbar(canvas, window)
        self.toolbar.addWidget(self.button_help)

    def help_button_click(self):
        if self.help_is_shown:
            self.help_panel.hide()
        else:
            self.help_panel.show()
        
        self.help_is_shown = not self.help_is_shown