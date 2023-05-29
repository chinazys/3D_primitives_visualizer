from PyQt5.QtWidgets import (QComboBox, QLabel, QVBoxLayout)

from ui.configurator.states.primitives_list.primitives_list import PrimitivesList
from ui.configurator.states.primitive_editor.primitive_editor import PrimitiveEditor
from util.clear_qt_layout import clear_qt_layout


class Configurator:
    """
    This module defines the `Configurator` class, which manages the state and layout of the configurator widget.

    The `Configurator` class has the following main components:
    - `primitives_list`: An instance of the `PrimitivesList` class, representing the list of active primitives.
    - `active_configurator`: A reference to the currently active configurator, which can be either `PrimitivesList` or `PrimitiveEditor`.
    - `on_configurator_state_changed`: Method that handles the state change in the configurator, updating the active configurator based on the mode (editor or list).

    Usage:
    1. Create an instance of `Configurator` by passing the window widget.
    2. The `Configurator` class manages the layout of the configurator, including the `PrimitivesList` widget as the initial active configurator.
    3. Call the `on_configurator_state_changed` method to switch between the editor and list mode.
    """
    CONFIGURATOR_LAYOUT_RELATIVE_WIDTH = 25
    
    def __init__(self, window):
        self.window = window
        self.primitives_list = PrimitivesList(self)
        self.active_configurator = self.primitives_list
        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, self.CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)
    
    def on_configurator_state_changed(self, is_editor, primitive=None, primitive_index=None):
        self.window.horizontal_layout.itemAt(2).layout().deleteLater()

        clear_qt_layout(self.active_configurator.vertical_layout)

        if is_editor:
            self.active_configurator = PrimitiveEditor(self, primitive, primitive_index)
        else:
            self.active_configurator = PrimitivesList(self)

        self.window.horizontal_layout.addLayout(self.active_configurator.vertical_layout, self.CONFIGURATOR_LAYOUT_RELATIVE_WIDTH)