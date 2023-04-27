from PyQt5.QtWidgets import (QComboBox, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtCore import pyqtSlot
from ui.configurator.configurator_types import *

class PrimitiveEditor(QWidget):
    def __init__(self, configurator):
        super().__init__()

        self.configurator = configurator

        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)
        
        self.primitive_type_selector = QComboBox()
        self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
        self.primitive_type_selector.currentTextChanged.connect(configurator.window.on_primitive_type_changed)
        self.vertical_layout.addWidget(self.primitive_type_selector)
        
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.setToolTip('Click to go back')
        self.cancel_button.clicked.connect(self.on_cancel_button_click)
        self.vertical_layout.addWidget(self.cancel_button)
    
    @pyqtSlot()
    def on_cancel_button_click(self):
        self.configurator.on_configurator_state_changed(False)