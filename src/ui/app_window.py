from matplotlib.figure import Figure

from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QWidget)
from PyQt5.QtCore import Qt

from ui.configurator.configurator import Configurator 
from ui.configurator.configurator_types import *
from ui.canvas.canvas import Canvas
from ui.settings import AXIS_MAX_SIZE

APP_WINDOW_ABSOLUTE_WIDTH = 1920
APP_WINDOW_ABSOLUTE_HEIGHT = 1080

class AppWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.window_width, self.window_height = APP_WINDOW_ABSOLUTE_WIDTH, APP_WINDOW_ABSOLUTE_HEIGHT
        
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 32px;
            }
        ''')        

        self.figure = Figure(figsize=(20, 20))
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        self.horizontal_layout = QHBoxLayout(self.central_widget)

        self.all_primitives = []

        self.canvas_layout = Canvas(self)

        self.configurator_layout = Configurator(self)

        self.ax = self.canvas_layout.canvas.figure.add_subplot(projection="3d")
        self.ax.set_xlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_ylim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)
        self.ax.set_zlim3d(-AXIS_MAX_SIZE, AXIS_MAX_SIZE)

        self.ax.view_init(30, 30)


    def on_primitive_added(self, primitive):
        primitive.build()
        primitive.plot(self.ax, self.canvas_layout.canvas, self.figure)
        
        self.all_primitives.append(primitive)

    def on_primitive_removed(self, index):
        print('Remove primitive #', index)
        # smth like self.all_primitives[index].remove() goes here
