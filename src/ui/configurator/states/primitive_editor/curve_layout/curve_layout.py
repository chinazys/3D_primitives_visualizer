from PyQt5.QtWidgets import (QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from primitives.curve.curve import Curve
from ui.configurator.states.primitive_editor.text_field.text_field import TextField
                             
class CurveLayout:
    def __init__(self, curve_id='Curve:'):
        self.layout = QVBoxLayout()

        self.curve_name_layout = QHBoxLayout()
        self.curve_name_layout.setAlignment(Qt.AlignLeft)
        self.curve_name_label = QLabel(curve_id)
        self.curve_name_label.setFixedWidth(100)
        self.curve_name_layout.addWidget(self.curve_name_label)
        self.curve_name_input = TextField(hint='m')
        self.curve_name_input.text_field.setAlignment(Qt.AlignCenter)
        self.curve_name_input.text_field.setFixedWidth(60)
        self.curve_name_layout.addWidget(self.curve_name_input.text_field)
        self.layout.addLayout(self.curve_name_layout)

        self.x_layout = QHBoxLayout()
        self.x_layout.addWidget(QLabel('x(t) = '))
        self.x_input = TextField(hint='x(t) parametric equation')
        self.x_layout.addWidget(self.x_input.text_field)
        self.layout.addLayout(self.x_layout)

        self.y_layout = QHBoxLayout()
        self.y_layout.addWidget(QLabel('y(t) = '))
        self.y_input = TextField(hint='y(t) parametric equation')
        self.y_layout.addWidget(self.y_input.text_field)
        self.layout.addLayout(self.y_layout)

        self.z_layout = QHBoxLayout()
        self.z_layout.addWidget(QLabel('z(t) = '))
        self.z_input = TextField(hint='z(t) parametric equation')
        self.z_layout.addWidget(self.z_input.text_field)
        self.layout.addLayout(self.z_layout)

        self.t_layout = QHBoxLayout()
        self.t_min_input = TextField(hint='left bound')
        self.t_min_input.text_field.setAlignment(Qt.AlignCenter)
        self.t_layout.addWidget(self.t_min_input.text_field)
        self.t_layout.addWidget(QLabel('< t <'))
        self.t_max_input = TextField(hint='right bound')
        self.t_max_input.text_field.setAlignment(Qt.AlignCenter)
        self.t_layout.addWidget(self.t_max_input.text_field)
        self.layout.addLayout(self.t_layout)
    
    def get_primitive(self):
        curve_name = self.curve_name_input.text
        if len(curve_name) < 1:
            return None
        curve = Curve([self.x_input.text, self.y_input.text, self.z_input.text, self.t_min_input.text, self.t_max_input.text, '100'])
        try:
            curve.build()
            curve.primitive_name = curve_name
            return curve
        except:
            return None