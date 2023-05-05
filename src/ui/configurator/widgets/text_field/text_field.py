from PyQt5.QtWidgets import (QLineEdit,QLabel)



class TextField:
        def __init__(self, window):
                self.text_field=QLineEdit()
                self.label=QLabel("Text field:")
                self.text=''
                window.vertical_layout.addWidget(self.label)
                window.vertical_layout.addWidget(self.text_field)
                self.text_field.textChanged.connect(self.text_changed)

        def text_changed(self, text):
                self.text=text