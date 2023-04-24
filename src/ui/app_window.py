from matplotlib.figure import Figure

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget)
from PyQt5.QtCore import Qt

from primitives.line.line import Line
from primitives.curve.curve import Curve
from primitives.lineMove.lineMove import curve_line
from primitives.lineFixedMove.lineFixedMove import lineFixedMove
from primitives.linesByCurve.lineByCurve import LineByCurve
from primitives.plane.plane import Plane


from ui.configurator.configurator import Configurator, CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE, CONFIGURATOR_TYPE_LINEMOVE, CONFIGURATOR_TYPE_LINEBYCURVE, CONFIGURATOR_TYPE_LINEFIXEDMOVE, CONFIGURATOR_TYPE_PLANE
from ui.canvas.canvas import Canvas
from ui.settings import AXIS_MAX_SIZE
from ui.text_field.text_field import TextField

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
        self.configurator_layout.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.on_primitive_type_changed(CONFIGURATOR_TYPE_LINE)
        self.ax.view_init(30, 30)



    def on_primitive_type_changed(self, configurator_type):
        if configurator_type == CONFIGURATOR_TYPE_LINE:
            self.active_primitive = Line([(0, 0, 0), (10, 10, 10)])
        elif configurator_type == CONFIGURATOR_TYPE_CURVE:
            self.active_primitive = Curve(['(t^2 + 1) * sin(t)', '(t^2 + 1) * cos(t)', 't'])
        elif configurator_type == CONFIGURATOR_TYPE_LINEMOVE:
            curve = Curve(['t', 'sin(t)', '5'])
            self.active_primitive = curve_line(curve, [1, 1, 1], [1, 1, 1])
        elif configurator_type == CONFIGURATOR_TYPE_LINEBYCURVE:
            curve = Curve(['t', 'sin(t)', '5'])
            line = Line([(-0.5, -0.5, -0.5), [0.5, 0.5, 0.5]])
            self.active_primitive = LineByCurve(curve,line)
        elif configurator_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE:
            curve = Curve(['t', 'sin(t)', '5'])
            self.active_primitive = lineFixedMove(curve, [0,0,60])
        elif configurator_type == CONFIGURATOR_TYPE_PLANE:
            self.active_primitive = Plane((5, 2, 0), (0, 0, 50))

        self.active_primitive.build()

        # to avoid plots stacking
        try: 
            self.ax.clear()
        except:
            pass

        self.ax = self.canvas_layout.canvas.figure.add_subplot(projection="3d")
        self.ax.set_xlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_ylim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_zlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        
        self.active_primitive.plot(self.ax, self.canvas_layout.canvas)
