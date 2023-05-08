from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.line.line import Line
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.states.primitive_editor.separator.separator import PaddedSeparator

class LineLayout:
    def __init__(self):
        self.layout = QVBoxLayout()
        
        self.point_a_layout = PointLayout(point_letter='A', point_id='Start Point:')
        self.layout.addLayout(self.point_a_layout.layout)

        self.separator = PaddedSeparator()
        self.layout.addLayout(self.separator.layout)

        self.point_b_layout = PointLayout(point_letter='B', point_id='End Point:')
        self.layout.addLayout(self.point_b_layout.layout)

    def get_primitive(self):
        try:
            point_a = self.point_a_layout.get_primitive()
            point_b = self.point_b_layout.get_primitive()
            
            if point_a is None or point_b is None:
                return None
            
            return Line([point_a, point_b])
        except:
            return None