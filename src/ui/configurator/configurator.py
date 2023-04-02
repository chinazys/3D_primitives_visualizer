from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)

CONFIGURATOR_TYPE_LINE = 'Line'
CONFIGURATOR_TYPE_CURVE = 'Curve'
CONFIGURATOR_TYPES = [CONFIGURATOR_TYPE_LINE, CONFIGURATOR_TYPE_CURVE]

class Configurator:
    def __init__(self, window):
        self.combo = QComboBox()
        self.combo.addItems(CONFIGURATOR_TYPES)
        
        rlayout = QVBoxLayout()
        window.layout.addLayout(rlayout, 30)
        rlayout.setContentsMargins(1, 1, 1, 1)
        rlayout.addWidget(QLabel("Plot type:"))
        rlayout.addWidget(self.combo)

        self.combo.currentTextChanged.connect(window.on_primitive_type_changed)