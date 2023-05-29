from PyQt5.QtWidgets import (QFrame, QVBoxLayout) 
from PyQt5.QtGui import (QColor, QPalette)

class Separator(QFrame):
    """A horizontal separator line widget.

    - Attributes:
        - thickness (int): The thickness of the separator line.
        - color (QColor): The color of the separator line.

    - Methods:
        - __init__(thickness, parent, color): Initialize a Separator object.
        - setColor(color): Set the color of the separator line.

    """
    def __init__(self, thickness, parent=None, color=QColor("grey")):
        super(Separator, self).__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(thickness)        
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

class PaddedSeparator:
    """A padded separator line widget.

    - Attributes:
        - layout (QVBoxLayout): The layout for the padded separator.

    - Methods:
        - __init__(thickness=2, vertical_padding=20, horizontal_padding=0): Initialize a PaddedSeparator object.

    """
    def __init__(self, thickness=2, vertical_padding=20, horizontal_padding=0):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(horizontal_padding, vertical_padding, horizontal_padding, vertical_padding)
        self.layout.addWidget(Separator(thickness))