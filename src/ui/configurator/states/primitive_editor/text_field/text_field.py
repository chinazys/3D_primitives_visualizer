from PyQt5.QtWidgets import (QLineEdit)

class TextField:
        """A custom text field widget for inputting text.
        - Attributes:
                - text_field (QLineEdit): The QLineEdit widget for text input.
                - initial_value (str): The initial value of the text field.
                - hint (str): The placeholder hint text for the text field.
                - text (str): The current text value of the text field.

        - Methods:
                - __init__(initial_value, hint): Initialize a TextField object.
                - set_text(text): Set the text value of the text field.
                - get_text() -> str: Get the current text value of the text field.
                - text_changed(text): Update the text value when the text field is changed.

        """

        def __init__(self, initial_value=None, hint=None):
                self.text_field=QLineEdit()
                self.initial_value = initial_value
                self.hint = hint
                
                self.text = ''
                if not self.hint is None:
                        self.text_field.setPlaceholderText(self.hint) 
                if not self.initial_value is None:
                        self.text = initial_value
                        self.text_field.setText(self.initial_value)
                        
                self.text_field.textChanged.connect(self.text_changed)

        def set_text(self, text):
                self.text_field.setText(text)

        def get_text(self):
                return self.text

        def text_changed(self, text):
                self.text = text