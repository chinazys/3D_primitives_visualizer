from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.lineMove.lineMove import curve_line
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.states.primitive_editor.separator.separator import PaddedSeparator

class CylindricalSurfaceLayout:
    def __init__(self):
        self.layout = QVBoxLayout()
        
        self.curve_layout = CurveLayout(curve_id='Curve:')
        self.layout.addLayout(self.curve_layout.layout)

        self.separator1 = PaddedSeparator()
        self.layout.addLayout(self.separator1.layout)

        self.point_layout = PointLayout(point_letter='P', point_id='Point:')
        self.layout.addLayout(self.point_layout.layout)

        self.separator2 = PaddedSeparator()
        self.layout.addLayout(self.separator2.layout)

        self.vector_layout = PointLayout(point_letter='v', point_id='Vector:')
        self.layout.addLayout(self.vector_layout.layout)

    def get_primitive(self):
        try:
            curve = self.curve_layout.get_primitive()
            point = self.point_layout.get_primitive()
            vector = self.vector_layout.get_primitive()
            
            if curve is None or point is None or vector is None:
                return None

            return curve_line(curve, point, vector)
        except:
            return None