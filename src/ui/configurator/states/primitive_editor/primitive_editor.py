from PyQt5.QtWidgets import (QComboBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from ui.configurator.configurator_types import *
from ui.configurator.states.primitive_editor.text_field.text_field import TextField
from ui.configurator.states.primitive_editor.point_text_field.point_text_field import PointTextField
from primitives.line.line import Line
from primitives.curve.curve import Curve
from primitives.lineMove.lineMove import curve_line
from primitives.lineFixedMove.lineFixedMove import lineFixedMove
from primitives.linesByCurve.lineByCurve import LineByCurve
from primitives.rotate_surface.rotate_surface import rotate_surface
from primitives.plane.plane import Plane

class PrimitiveEditor(QWidget):
    def __init__(self, configurator):
        super().__init__()

        self.configurator = configurator

        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)

        self.top_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.top_vertical_layout)
        self.top_vertical_layout.setAlignment(Qt.AlignTop)

        self.center_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.center_vertical_layout)
        self.center_vertical_layout.setAlignment(Qt.AlignVCenter)

        self.bottom_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.bottom_vertical_layout)
        self.bottom_vertical_layout.setAlignment(Qt.AlignBottom)

        self.primitive_type_selector = QComboBox()
        self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
        self.primitive_type = CONFIGURATOR_TYPES[0]
        self.primitive_type_selector.currentTextChanged.connect(self.on_primitive_type_changed)
        self.top_vertical_layout.addWidget(self.primitive_type_selector)
        
        self.name_text_field = TextField()
        self.center_vertical_layout.addWidget(self.name_text_field.text_field)
        
        self.point_text_field = PointTextField()
        self.center_vertical_layout.addLayout(self.point_text_field.base)
    
        self.bottom_horizontal_layout = QHBoxLayout()
        self.bottom_vertical_layout.addLayout(self.bottom_horizontal_layout)

        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.setToolTip('Click to go back')
        self.cancel_button.clicked.connect(self.on_cancel_button_click)
        self.bottom_horizontal_layout.addWidget(self.cancel_button)
        
        self.confirm_button = QPushButton('Confirm', self)
        self.confirm_button.setToolTip('Click to plot')
        self.confirm_button.clicked.connect(self.on_confirm_button_click)
        self.bottom_horizontal_layout.addWidget(self.confirm_button)

    def on_primitive_type_changed(self, primitive_type):
        self.primitive_type = primitive_type

    @pyqtSlot()
    def on_cancel_button_click(self):
        self.configurator.on_configurator_state_changed(False)
    
    @pyqtSlot()
    def on_confirm_button_click(self):
        if len(self.name_text_field.text) < 1:
            return
                
        if self.primitive_type == CONFIGURATOR_TYPE_LINE:
            primitive = Line([(0, 0, 0), (10, 10, 10)])
        elif self.primitive_type == CONFIGURATOR_TYPE_CURVE:
            primitive = Curve(['(t^2 + 1) * sin(t)', '(t^2 + 1) * cos(t)', 't', '-4', '12', '100'])
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEMOVE:
            curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
            primitive = curve_line(curve, [1, 0.8414709848078965, 5], [1, 1, 1])
        # elif self.primitive_type == CONFIGURATOR_TYPE_LINEBYCURVE:
        #     curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
        #     line = Line([(-0.5, -0.5, -0.5), [0.5, 0.5, 0.5]])
        #     primitive = LineByCurve(curve,line)
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE:
            curve = Curve(['50*cos(t)', '50*sin(t)', '-20', '0', '6.29', '100'])
            primitive = lineFixedMove(curve, [0,0,100])
        elif self.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
            curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
            primitive = rotate_surface(curve, [1, 0.8414709848078965, 5], [1, 1, 1])
        elif self.primitive_type == CONFIGURATOR_TYPE_PLANE:
            primitive = Plane((5, 2, 0), (0, 0, 50))
        else:
            raise Exception('Unknown primitive type')

        primitive.primitive_name = self.name_text_field.text
        primitive.primitive_type = self.primitive_type

        self.configurator.window.on_primitive_added(primitive)
        self.configurator.on_configurator_state_changed(False)