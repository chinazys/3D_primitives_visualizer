from PyQt5.QtWidgets import (QComboBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from ui.configurator.configurator_types import *
from ui.configurator.states.primitive_editor.text_field.text_field import TextField

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
        self.primitive_type_selector.currentTextChanged.connect(configurator.window.on_primitive_type_changed)
        self.top_vertical_layout.addWidget(self.primitive_type_selector)
        
        self.text_field = TextField()
        self.center_vertical_layout.addWidget(self.text_field.text_field)
    
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

    @pyqtSlot()
    def on_cancel_button_click(self):
        self.configurator.on_configurator_state_changed(False)
    
    @pyqtSlot()
    def on_confirm_button_click(self):
        print('=')