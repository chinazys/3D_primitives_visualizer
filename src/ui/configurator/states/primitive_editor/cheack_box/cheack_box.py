from PyQt5.QtWidgets import (QHBoxLayout, QCheckBox)

class CheackboxLayout:
    def __init__(self,window ,text:str):
        self.base = QHBoxLayout()
        self.cheack_box=QCheckBox(text)
        self.base.addWidget(self.cheack_box)
        window.vertical_layout.addLayout(self.base)
        self.cheack_box.stateChanged.connect(lambda: self.chang_state(self.cheack_box))

    def chang_state(self,c):
        if c.isChecked() == True:
            return True
        else:
            return False
