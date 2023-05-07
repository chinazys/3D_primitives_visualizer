from PyQt5.QtWidgets import (QVBoxLayout, QLabel)

from ui.configurator.states.primitive_editor.text_field.text_field import TextField

class NameLayout:
    def __init__(self):
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Primitive name:'))

        self.input_field = TextField(hint="e.g. MyPrimitive")
        self.layout.addWidget(self.input_field.text_field)