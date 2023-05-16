from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSlot

from ui.configurator.states.primitives_list.primitive_info.primitive_info import PrimitiveInfo
from ui.configurator.separator.separator import PaddedSeparator
from util.clear_qt_layout import clear_qt_layout

class PrimitivesList(QWidget):
    def __init__(self, configurator):
        super().__init__()
        
        self.configurator = configurator

        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)

        self.top_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.top_vertical_layout)
        self.top_vertical_layout.setAlignment(Qt.AlignTop)

        self.set_top_label_layout()
        self.top_vertical_layout.addLayout(self.top_label_layout)

        self.separator = PaddedSeparator(vertical_padding=8)
        self.top_vertical_layout.addLayout(self.separator.layout)

        self.bottom_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.bottom_vertical_layout)
        self.bottom_vertical_layout.setAlignment(Qt.AlignBottom)

        self.primitive_info_list = []

        for i, primitive in enumerate(self.configurator.window.all_primitives):
            self.primitive_info_list.append(PrimitiveInfo(primitive, i, self, top_offset=10))
            self.top_vertical_layout.addLayout(self.primitive_info_list[-1].base)

        self.add_button = QPushButton('Add', self)
        self.add_button.setToolTip('Click to add a new primitive')
        self.add_button.clicked.connect(self.on_add_button_click)
        self.bottom_vertical_layout.addWidget(self.add_button)

    def set_top_label_layout(self):
        self.top_label_layout = QHBoxLayout()
        self.top_label = QLabel('Active Primitives')
        self.top_label.setContentsMargins(0, 6, 0, 0)
        self.top_label.setFont(QFont('Arial', 20))
        self.top_label_layout.addWidget(self.top_label)     
        self.top_label_layout.setAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def on_add_button_click(self):
        self.configurator.on_configurator_state_changed(True)

    def on_delete_primitive_button_click(self, primitive_index):
        self.configurator.window.on_primitive_removed(primitive_index)
        
        for i in range(primitive_index + 1, len(self.primitive_info_list)):
            self.primitive_info_list[i].index = self.primitive_info_list[i].index - 1

        clear_qt_layout(self.primitive_info_list[primitive_index].base)

        del(self.primitive_info_list[primitive_index])