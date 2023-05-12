from PyQt5.QtWidgets import (QHBoxLayout, QCheckBox)

class CheckBoxLayout:
    def __init__(self, text:str):
        self.base = QHBoxLayout()
        self.check_box=QCheckBox(text)
        self.check_box.setStyleSheet("QCheckBox::indicator { width: 24 px; height: 24 px;}")
        self.base.addWidget(self.check_box)
        self.check_box.stateChanged.connect(lambda: self.change_state(self.check_box))

    def change_state(self, c):
        if c.isChecked() == True:
            return True
        else:
            return False
