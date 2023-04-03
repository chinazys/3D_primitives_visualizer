from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import (QVBoxLayout)

from ui.tool_bar.tool_bar import ToolBar

CANVAS_LAYOUT_RELATIVE_WIDTH = 75

class Canvas:
    def __init__(self, window):
        self.canvas = FigureCanvas(window.figure)
        
        self.vertical_layout = QVBoxLayout()
        window.horizontal_layout.addLayout(self.vertical_layout, CANVAS_LAYOUT_RELATIVE_WIDTH)
        self.toolbar = ToolBar(self.canvas, window)

        self.vertical_layout.addWidget(self.toolbar.toolbar)
        self.vertical_layout.addWidget(self.canvas)
