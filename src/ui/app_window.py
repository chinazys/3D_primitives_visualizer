from matplotlib.figure import Figure

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget)

from primitives.line.line import Line
from primitives.curve.curve import Curve
from ui.configurator.configurator import Configurator, CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE
from ui.canvas.canvas import Canvas

AXIS_MAX_SIZE = 100

APP_WINDOW_ABSOLUTE_WIDTH = 1920
APP_WINDOW_ABSOLUTE_HEIGHT = 1080

class AppWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.window_width, self.window_height = APP_WINDOW_ABSOLUTE_WIDTH, APP_WINDOW_ABSOLUTE_HEIGHT
        
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 25px;
            }
        ''')        

        self.figure = Figure(figsize=(20, 20))
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        self.horizontal_layout = QHBoxLayout(self.central_widget)

        self.canvas_layout = Canvas(self)
        self.configurator_layout = Configurator(self)

        self.on_primitive_type_changed(CONFIGURATOR_TYPE_LINE)
        self.ax.view_init(30, 30)

    def on_primitive_type_changed(self, configurator_type):
        if configurator_type == CONFIGURATOR_TYPE_LINE:
            self.active_primitive = Line([(0, 0, 0), [10, 10, 10]])
        elif configurator_type == CONFIGURATOR_TYPE_CURVE:
            self.active_primitive = Curve([1.5, 2, 1])

        self.active_primitive.build()

        self.ax = self.canvas_layout.canvas.figure.add_subplot(projection="3d")
        self.ax.set_xlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_ylim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_zlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        
        self.active_primitive.plot(self.ax, self.canvas_layout.canvas)
