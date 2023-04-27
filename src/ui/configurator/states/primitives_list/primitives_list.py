from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QPushButton, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from ui.configurator.states.primitives_list.primitive_info.primitive_info import PrimitiveInfo

class PrimitivesList(QWidget):
    def __init__(self, configurator):
        super().__init__()
        
        self.configurator = configurator

        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)

        self.top_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.top_vertical_layout)
        self.top_vertical_layout.setAlignment(Qt.AlignTop)

        self.bottom_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.bottom_vertical_layout)
        self.bottom_vertical_layout.setAlignment(Qt.AlignBottom)

        self.top_vertical_layout.addWidget(QLabel('Active Primitives List:'))
        self.primitive_info = PrimitiveInfo(primitiv_name='Some Primitive')
        self.top_vertical_layout.addLayout(self.primitive_info.base)

        self.add_button = QPushButton('Add', self)
        self.add_button.setToolTip('Click to add a new primitive')
        self.add_button.clicked.connect(self.on_add_button_click)
        self.bottom_vertical_layout.addWidget(self.add_button)

    @pyqtSlot()
    def on_add_button_click(self):
        self.configurator.on_configurator_state_changed(True)