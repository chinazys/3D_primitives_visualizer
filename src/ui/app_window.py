from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QWidget)

from primitives.surface.surface import Surface
from primitives.line.line import Line
from primitives.curve.curve import Curve
from ui.menu_bar.menu_bar import MenuBar
from ui.configurator.configurator import Configurator, CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE

class AppWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.window_width, self.window_height = 1700, 800
        
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 25px;
            }
        ''')        

        self.figure = Figure(figsize=(20, 20))
        self.canvas = FigureCanvas(self.figure)
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.addWidget(self.canvas, 88)

        MenuBar(self, app)

        Configurator(self)

        self.on_primitive_type_changed(CONFIGURATOR_TYPE_LINE)
        self.ax.view_init(30, 30)

    def on_primitive_type_changed(self, configurator_type):
        if configurator_type == CONFIGURATOR_TYPE_LINE:
            self.active_primitive = Line([(0, 0, 0), [10, 10, 10]])
        elif configurator_type == CONFIGURATOR_TYPE_CURVE:
            self.active_primitive = Curve([1.5, 2, 1])

        self.active_primitive.build()

        self.ax = self.canvas.figure.add_subplot(projection="3d")
        self.active_primitive.plot(self.ax, self.canvas)
