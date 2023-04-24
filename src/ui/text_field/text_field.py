from PyQt5.QtWidgets import (QLineEdit,QVBoxLayout,QLabel)



class TextField:
        def __init__(self, window):
                self.text_field=QLineEdit()
                self.label=QLabel("Text field:")
                self.vertical_layout = QVBoxLayout()
                #window.horizontal_layout.addLayout(self.vertical_layout, 25)
                self.text=''
                #self.text_field.setAlignment(Qt.AlignmentFlag.AlignTop)
                self.text_field.textChanged.connect(self.text_changed)

        def text_changed(self, text):
                self.text=text