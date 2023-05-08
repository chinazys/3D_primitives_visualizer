from PyQt5.QtWidgets import (QFrame, QVBoxLayout) 
from PyQt5.QtGui import (QColor, QPalette)

class Separator(QFrame):
    def __init__(self, parent=None, color=QColor("grey")):
        super(Separator, self).__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(2)        
        self.setContentsMargins(0, 200, 0, 200)
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class PaddedSeparator:
    def __init__(self, vertical_padding=20, horizontal_padding=0):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(horizontal_padding, vertical_padding, horizontal_padding, vertical_padding)
        self.layout.addWidget(Separator())