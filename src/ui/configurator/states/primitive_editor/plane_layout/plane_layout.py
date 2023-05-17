from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.plane.plane import Plane
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.separator.separator import PaddedSeparator

class PlaneLayout:
    def __init__(self, initial_primitive):
        if initial_primitive is None:
            point = None
            vector = None
        else:
            point = initial_primitive.M
            vector = initial_primitive.n
            
        self.layout = QVBoxLayout()
        
        self.point_layout = PointLayout(point_letter='M', point_id='Point:')
        if not point is None:
            self.point_layout.set_point(point)
        self.layout.addLayout(self.point_layout.layout)

        self.separator = PaddedSeparator()
        self.layout.addLayout(self.separator.layout)

        self.vector_layout = PointLayout(point_letter='n', point_id='Vector:')
        if not vector is None:
            self.vector_layout.set_point(vector)
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