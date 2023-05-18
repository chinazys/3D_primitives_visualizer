from PyQt5.QtWidgets import (QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from primitives.curve.curve import Curve
from ui.configurator.states.primitive_editor.text_field.text_field import TextField
                             
class CurveLayout:
    def __init__(self, initial_primitive, curve_label="Curve:"):
        if initial_primitive is None:
            initial_curve_name = None
            initial_x_text = None
            initial_y_text = None
            initial_z_text = None
            initial_t_min_text = None
            initial_t_max_text = None
        else:
            initial_curve_name = initial_primitive.primitive_name
            initial_x_text = initial_primitive.x_string
            initial_y_text = initial_primitive.y_string
            initial_z_text = initial_primitive.z_string
            initial_t_min_text = initial_primitive.t_min_string
            initial_t_max_text = initial_primitive.t_max_string

        self.curve_label = curve_label

        self.layout = QVBoxLayout()

        if not self.curve_label is None:
            self.curve_name_layout = QHBoxLayout()
            self.curve_name_layout.setAlignment(Qt.AlignLeft)
            self.curve_name_label = QLabel(curve_label)
            self.curve_name_label.setFixedWidth(100)
            self.curve_name_layout.addWidget(self.curve_name_label)
            self.curve_name_input = TextField(hint='m', initial_value=initial_curve_name)
            self.curve_name_input.text_field.setAlignment(Qt.AlignCenter)
            self.curve_name_input.text_field.setFixedWidth(60)
            self.curve_name_layout.addWidget(self.curve_name_input.text_field)
            self.layout.addLayout(self.curve_name_layout)

        self.x_layout = QHBoxLayout()
        self.x_layout.addWidget(QLabel('x(t) = '))
        self.x_input = TextField(hint='x(t) parametric equation', initial_value=initial_x_text)
        self.x_layout.addWidget(self.x_input.text_field)
        self.layout.addLayout(self.x_layout)

        self.y_layout = QHBoxLayout()
        self.y_layout.addWidget(QLabel('y(t) = '))
        self.y_input = TextField(hint='y(t) parametric equation', initial_value=initial_y_text)
        self.y_layout.addWidget(self.y_input.text_field)
        self.layout.addLayout(self.y_layout)

        self.z_layout = QHBoxLayout()
        self.z_layout.addWidget(QLabel('z(t) = '))
        self.z_input = TextField(hint='z(t) parametric equation', initial_value=initial_z_text)
        self.z_layout.addWidget(self.z_input.text_field)
        self.layout.addLayout(self.z_layout)

        self.t_layout = QHBoxLayout()
        self.t_min_input = TextField(hint='left bound', initial_value=initial_t_min_text)
        self.t_min_input.text_field.setAlignment(Qt.AlignCenter)
        self.t_layout.addWidget(self.t_min_input.text_field)
        self.t_layout.addWidget(QLabel('< t <'))
        self.t_max_input = TextField(hint='right bound', initial_value=initial_t_max_text)
        self.t_max_input.text_field.setAlignment(Qt.AlignCenter)
        self.t_layout.addWidget(self.t_max_input.text_field)
        self.layout.addLayout(self.t_layout)
    
    def get_primitive(self):
        if not self.curve_label is None:
            curve_name = self.curve_name_input.text
            if len(curve_name) < 1:
                return None
        
        curve = Curve([self.x_input.get_text(), self.y_input.get_text(), self.z_input.get_text(), self.t_min_input.get_text(), self.t_max_input.get_text(), '100'])
        
        try:
            curve.build()
            if not self.curve_label is None:
                curve.primitive_name = curve_name
            return curve
        except:
            print('error')
            return None