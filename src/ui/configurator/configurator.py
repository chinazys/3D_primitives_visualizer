from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)
from ui.text_field.text_field import TextField
from PyQt5.QtCore import Qt

CONFIGURATOR_TYPE_LINE = 'Line'
CONFIGURATOR_TYPE_CURVE = 'Curve'
CONFIGURATOR_TYPE_LINEMOVE = 'Line move'
CONFIGURATOR_TYPE_LINEFIXEDMOVE = 'Fixed move of line'
CONFIGURATOR_TYPE_LINEBYCURVE = 'Line by curve'
CONFIGURATOR_TYPE_PLANE = 'Plane'
CONFIGURATOR_TYPES = [CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE, CONFIGURATOR_TYPE_LINEMOVE,
                      CONFIGURATOR_TYPE_LINEBYCURVE, CONFIGURATOR_TYPE_LINEFIXEDMOVE, CONFIGURATOR_TYPE_PLANE]


CONFIGURATOR_LAYOUT_RELATIVE_WIDTH = 25

class Configurator:
    def __init__(self, window):
        self.primitive_type_selector = QComboBox()
        self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
        
        self.vertical_layout = QVBoxLayout()
        window.horizontal_layout.addLayout(self.vertical_layout, CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)
        self.text_field_layout = TextField(self)
        self.vertical_layout.addWidget(self.text_field_layout.label)
        self.vertical_layout.addWidget(self.text_field_layout.text_field)
        self.vertical_layout.addWidget(QLabel("Plot type:"))
        self.vertical_layout.addWidget(self.primitive_type_selector)

        self.primitive_type_selector.currentTextChanged.connect(window.on_primitive_type_changed)