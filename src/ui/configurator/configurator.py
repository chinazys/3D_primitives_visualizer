from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)

from ui.configurator.states.primitives_list.primitives_list import PrimitivesList
from ui.configurator.states.primitive_editor.primitive_editor import PrimitiveEditor
from util.clear_qt_layout import clear_qt_layout


class Configurator:
    CONFIGURATOR_LAYOUT_RELATIVE_WIDTH = 25
    
    def __init__(self, window):
        self.window = window
        self.primitives_list = PrimitivesList(self)
        self.active_configurator = self.primitives_list
        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, self.CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
    
    def on_configurator_state_changed(self, is_editor):
        self.window.horizontal_layout.itemAt(2).layout().deleteLater()

        clear_qt_layout(self.active_configurator.vertical_layout)

        if is_editor:
            self.active_configurator = PrimitiveEditor(self)
        else:
            self.active_configurator = PrimitivesList(self)

        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, self.CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)