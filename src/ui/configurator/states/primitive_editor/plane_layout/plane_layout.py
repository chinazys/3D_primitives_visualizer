from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.plane.plane import Plane
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.states.primitive_editor.separator.separator import PaddedSeparator

class PlaneLayout:
    def __init__(self):
        self.layout = QVBoxLayout()
        
        self.point_layout = PointLayout(point_letter='M', point_id='Point:')
        self.layout.addLayout(self.point_layout.layout)

        self.separator = PaddedSeparator()
        self.layout.addLayout(self.separator.layout)

        self.vector_layout = PointLayout(point_letter='n', point_id='Vector:')
        self.layout.addLayout(self.vector_layout.layout)

    def get_primitive(self):
        try:
            point = self.point_layout.get_primitive()
            vector = self.vector_layout.get_primitive()
            
            if point is None or vector is None:
                return None
            
            return Plane(point, vector)
        except:
            return None