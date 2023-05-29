from PyQt5.QtWidgets import (QHBoxLayout, QCheckBox)

class CheckBoxLayout:
    """A layout containing a checkbox widget.

    - Attributes:
        - base (QHBoxLayout): The base layout for the checkbox.
        - check_box (QCheckBox): The checkbox widget.

    - Methods:
        - __init__(text: str): Initialize a CheckBoxLayout object.
        - set_state(state: bool): Set the state of the checkbox.
        - get_state() -> bool: Get the state of the checkbox.
        - change_state(c): Handle the state change event of the checkbox.

    """
    def __init__(self, text:str):
        self.base = QHBoxLayout()
        self.check_box=QCheckBox(text)
        self.check_box.setStyleSheet("QCheckBox::indicator { width: 24 px; height: 24 px;}")
        self.base.addWidget(self.check_box)
        self.check_box.stateChanged.connect(lambda: self.change_state(self.check_box))
    
    def set_state(self, state:bool):
        self.check_box.setChecked(state)
    
    def get_state(self):
        return self.check_box.isChecked()

    def change_state(self, c):
        if c.isChecked() == True:
            return True
        else:
            return False
