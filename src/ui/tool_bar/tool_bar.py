from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction

class ToolBar:
    def __init__(self, canvas, window):
        self.toolbar = NavigationToolbar(canvas, window)
