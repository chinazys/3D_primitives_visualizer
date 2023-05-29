from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.conical_surface.conical_surface import ConicalSurface
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.separator.separator import PaddedSeparator

class ConicalSurfaceLayout:
    """A layout for configuring a conical surface primitive.

    - Attributes:
        - layout (QVBoxLayout): The main layout for the conical surface layout.
        - curve_layout (CurveLayout): The layout for configuring the curve.
        - separator (PaddedSeparator): The separator layout.
        - point_layout (PointLayout): The layout for configuring the fixed point.

    - Methods:
        - __init__(initial_primitive): Initialize a ConicalSurfaceLayout object.
        - get_primitive() -> ConicalSurface: Get the configured conical surface primitive.

    """
    def __init__(self, initial_primitive):
        if initial_primitive is None:
            curve = None
            point = None
        else:
            curve = initial_primitive.base
            point = initial_primitive.fixdot

        self.layout = QVBoxLayout()
        
        self.curve_layout = CurveLayout(curve, curve_label='Curve:')
        self.layout.addLayout(self.curve_layout.layout)

        self.separator = PaddedSeparator()
        self.layout.addLayout(self.separator.layout)

        self.point_layout = PointLayout(point_letter='F', point_id='Fixed Point:')
        if not point is None:
            self.point_layout.set_point(point)
        self.layout.addLayout(self.point_layout.layout)

    def get_primitive(self):
        try:
            curve = self.curve_layout.get_primitive()
            point = self.point_layout.get_primitive()

            if curve is None or point is None:
                return None
            
            return ConicalSurface(curve, point)
        except:
            return None