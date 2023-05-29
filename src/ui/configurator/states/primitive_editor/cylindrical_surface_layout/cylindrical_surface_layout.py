from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.cylindrical_surface.cylindrical_surface import CylindricalSurface
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.separator.separator import PaddedSeparator

class CylindricalSurfaceLayout:
    """A layout for configuring a cylindrical surface primitive.

    - Attributes:
        - layout (QVBoxLayout): The main layout for the cylindrical surface layout.
        - curve_layout (CurveLayout): The layout for configuring the base curve.
        - separator1 (PaddedSeparator): The separator between the base curve and point layout.
        - point_layout (PointLayout): The layout for configuring the point.
        - separator2 (PaddedSeparator): The separator between the point layout and vector layout.
        - vector_layout (PointLayout): The layout for configuring the vector.

    - Methods:
        - __init__(initial_primitive): Initialize a CylindricalSurfaceLayout object.
        - get_primitive() -> CylindricalSurface: Get the configured cylindrical surface primitive.

    """
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

            return CylindricalSurface(curve, point, vector)
        except:
            return None