from PyQt5.QtWidgets import (QLineEdit,QVBoxLayout,QLabel)
from PyQt5.QtCore import Qt

#self.widget = QLineEdit()
        #self.widget.setMaxLength(10)
        #self.widget.setPlaceholderText("Enter your text")
        #self.set(self.widget)

class TextField:
        def __init__(self, window):
                self.text_field=QLineEdit()
                self.vertical_layout = QVBoxLayout()
                window.horizontal_layout.addLayout(self.vertical_layout, 25)
                self.vertical_layout.setContentsMargins(1, 1, 1, 1)
                self.vertical_layout.addWidget(QLabel("Text field:"))
                self.vertical_layout.addWidget(self.text_field)
                self.text=''
                #self.text_field.setAlignment(Qt.AlignmentFlag.AlignTop)
                self.text_field.textChanged.connect(self.text_changed)

        def text_changed(self, text):
                self.text=text