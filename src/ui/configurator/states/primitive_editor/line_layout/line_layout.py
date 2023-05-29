from PyQt5.QtWidgets import (QVBoxLayout)

from primitives.line.line import Line
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.separator.separator import PaddedSeparator

class LineLayout:
    """A layout for configuring a line primitive.

    - Attributes:
        - layout (QVBoxLayout): The main layout for the line layout.
        - point_a_layout (PointLayout): The layout for configuring the start point.
        - point_b_layout (PointLayout): The layout for configuring the end point.
        - separator (PaddedSeparator): The separator between the start point and end point layouts.

    - Methods:
        - __init__(initial_primitive): Initialize a LineLayout object.
        - get_primitive() -> Line: Get the configured line primitive.

    """
    def __init__(self, initial_primitive):
        self.layout = QVBoxLayout()
        
        self.point_a_layout = PointLayout(point_letter='A', point_id='Start Point:')
        self.point_b_layout = PointLayout(point_letter='B', point_id='End Point:')
        if not initial_primitive is None:
            self.point_a_layout.set_point(initial_primitive.a_point)
            self.point_b_layout.set_point(initial_primitive.b_point)

        self.layout.addLayout(self.point_a_layout.layout)

        self.separator = PaddedSeparator()
        self.layout.addLayout(self.separator.layout)

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