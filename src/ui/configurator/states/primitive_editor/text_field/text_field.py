from PyQt5.QtWidgets import (QLineEdit)

class TextField:
        def __init__(self):
                self.text_field=QLineEdit()
                self.text=''
                self.text_field.setPlaceholderText('//TODO') 
                self.text_field.textChanged.connect(self.text_changed)

        def text_changed(self, text):
                self.text=text