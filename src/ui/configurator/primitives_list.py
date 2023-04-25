from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QWidget, QPushButton)
from PyQt5.QtCore import pyqtSlot

class PrimitivesList(QWidget):
    def __init__(self, configurator):
        super().__init__()
        
        self.configurator = configurator

        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)

        self.add_button = QPushButton('Add', self)
        self.add_button.setToolTip('Click to add a new primitive')
        self.add_button.clicked.connect(self.on_add_button_click)
        self.vertical_layout.addWidget(self.add_button)

    @pyqtSlot()
    def on_add_button_click(self):
        self.configurator.on_configurator_state_changed(True)