from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import (QVBoxLayout)

from ui.canvas.tool_bar.tool_bar import ToolBar

from PyQt5.QtCore import Qt

CANVAS_LAYOUT_RELATIVE_WIDTH = 75

class Canvas:
    """A canvas widget for displaying a matplotlib figure.

    - Attributes:
        - canvas (FigureCanvas): An instance of FigureCanvasQTAgg representing the canvas for displaying the figure.
        - vertical_layout (QVBoxLayout): A QVBoxLayout object for organizing the toolbar and canvas vertically.
        - toolbar (ToolBar): An instance of the ToolBar class representing the toolbar for the canvas.

    - Methods:
        - __init__(window): Initialize a Canvas object.

    """
    def __init__(self, window):
        self.canvas = FigureCanvas(window.figure)
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        
        self.vertical_layout = QVBoxLayout()
        window.horizontal_layout.addLayout(self.vertical_layout, CANVAS_LAYOUT_RELATIVE_WIDTH)
        self.toolbar = ToolBar(self.canvas, window)

        self.vertical_layout.addWidget(self.toolbar.toolbar)
        self.vertical_layout.addWidget(self.canvas)