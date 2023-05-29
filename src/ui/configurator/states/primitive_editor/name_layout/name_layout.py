from PyQt5.QtWidgets import (QHBoxLayout, QLabel)

from ui.configurator.states.primitive_editor.text_field.text_field import TextField

class NameLayout:
    """A layout for configuring the name of a primitive.

    - Attributes:
        - layout (QHBoxLayout): The main layout for the name layout.
        - input_field (TextField): The text field for entering the name.

    - Methods:
        - __init__(initial_name, label): Initialize a NameLayout object.
        - get_name() -> str: Get the entered name.

    """
    def __init__(self, initial_name, label='Name:  '):
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)

        self.layout.addWidget(QLabel(label))

        self.input_field = TextField(hint="e.g. MyPrimitive")
        if not initial_name is None:
            self.input_field.set_text(initial_name)
        self.layout.addWidget(self.input_field.text_field)
    
    def get_name(self):
        if len(self.input_field.get_text()) < 1:
            return None
        return self.input_field.get_text()