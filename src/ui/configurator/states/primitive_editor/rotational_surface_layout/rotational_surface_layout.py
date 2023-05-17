from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.rotate_surface.rotate_surface import rotate_surface
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.separator.separator import PaddedSeparator

class RotationalSurfaceLayout:
    def __init__(self, initial_primitive):
        if initial_primitive is None:
            curve = None
            point = None
            vector = None
        else:
            curve = initial_primitive.base
            point = initial_primitive.point_saved
            vector = initial_primitive.vector_saved

        self.layout = QVBoxLayout()
        
        self.curve_layout = CurveLayout(curve, curve_label='Curve:')
        self.layout.addLayout(self.curve_layout.layout)

        self.separator1 = PaddedSeparator()
        self.layout.addLayout(self.separator1.layout)

        self.point_layout = PointLayout(point_letter='P', point_id='Point:')
        if not point is None:
            self.point_layout.set_point(point)
        self.layout.addLayout(self.point_layout.layout)

        self.separator2 = PaddedSeparator()
        self.layout.addLayout(self.separator2.layout)

        self.vector_layout = PointLayout(point_letter='v', point_id='Vector:')
        if not vector is None:
            self.vector_layout.set_point(vector)
        self.layout.addLayout(self.vector_layout.layout)

    def get_primitive(self):
        try:
            curve = self.curve_layout.get_primitive()
            point = self.point_layout.get_primitive()
            vector = self.vector_layout.get_primitive()
            
            if curve is None or point is None or vector is None:
                return None
            
            return rotate_surface(curve, point, vector)
        except:
            return None