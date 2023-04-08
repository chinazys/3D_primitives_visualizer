from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)

CONFIGURATOR_TYPE_LINE = 'Line'
CONFIGURATOR_TYPE_CURVE = 'Curve'
CONFIGURATOR_TYPE_LINEMOVE = 'Line move'
CONFIGURATOR_TYPE_LINEFIXEDMOVE = 'Fixed move of line'
CONFIGURATOR_TYPES = [CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE, CONFIGURATOR_TYPE_LINEMOVE, CONFIGURATOR_TYPE_LINEFIXEDMOVE]

CONFIGURATOR_LAYOUT_RELATIVE_WIDTH = 25

class Configurator:
    def __init__(self, window):
        self.primitive_type_selector = QComboBox()
        self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
        
        self.vertical_layout = QVBoxLayout()
        window.horizontal_layout.addLayout(self.vertical_layout, CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)
        self.vertical_layout.addWidget(QLabel("Plot type:"))
        self.vertical_layout.addWidget(self.primitive_type_selector)

        self.primitive_type_selector.currentTextChanged.connect(window.on_primitive_type_changed)