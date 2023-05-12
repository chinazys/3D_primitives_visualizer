from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)

from ui.configurator.states.primitives_list.primitives_list import PrimitivesList
from ui.configurator.states.primitive_editor.primitive_editor import PrimitiveEditor

CONFIGURATOR_LAYOUT_RELATIVE_WIDTH = 25

class Configurator:
    def __init__(self, window):
        self.window = window
        self.primitives_list = PrimitivesList(self)
        self.active_configurator = self.primitives_list
        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
    
    def on_configurator_state_changed(self, isEditor):
        self.window.horizontal_layout.itemAt(2).layout().deleteLater()

        Configurator.clear_layout(self.active_configurator.vertical_layout)

        if isEditor:
            self.active_configurator = PrimitiveEditor(self)
        else:
            self.active_configurator = PrimitivesList(self)

        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
    
    def clear_layout(layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                Configurator.clear_layout(item.layout())