from PyQt5.QtWidgets import (QLabel, QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import Qt

from primitives.point.point import Point
from ui.configurator.states.primitive_editor.text_field.text_field import TextField

class PointLayout:
    """A layout for configuring a point primitive.

    - Attributes:
        - layout (QVBoxLayout): The main layout for the point layout.
        - base (QHBoxLayout): The layout for configuring the point.
        - point_name_input (TextField): The input field for the point name.
        - X_field (QLineEdit): The input field for the x coordinate.
        - Y_field (QLineEdit): The input field for the y coordinate.
        - Z_field (QLineEdit): The input field for the z coordinate.
        - x (str): The value of the x coordinate.
        - y (str): The value of the y coordinate.
        - z (str): The value of the z coordinate.

    - Methods:
        - __init__(point_letter, point_id): Initialize a PointLayout object.
        - text_changed_x(text): Update the x coordinate value.
        - text_changed_y(text): Update the y coordinate value.
        - text_changed_z(text): Update the z coordinate value.
        - set_point(point): Set the values of the point coordinates.
        - get_primitive() -> Point: Get the configured point primitive.

    """
    def __init__(self, point_letter="A", point_id='Point:'):
        self.layout = QVBoxLayout()
        # self.layout.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(QLabel(point_id))
        self.base = QHBoxLayout()
        self.layout.addLayout(self.base)
        self.base.setSpacing(0)
        self.point_name_input = TextField(hint=point_letter)
        self.point_name_input.text_field.setFixedWidth(50)
        self.point_name_input.text_field.setAlignment(Qt.AlignCenter)
        self.base.addWidget(self.point_name_input.text_field)
        self.FSegment=QLabel(" = (")
        self.base.addWidget(self.FSegment)
        self.FSegment.setFixedWidth(60)
        self.x=None; self.y=None; self.z=None
        self.X_field=QLineEdit()
        self.base.addWidget(self.X_field)
        self.X_field.setFixedWidth(70)
        self.X_field.setAlignment(Qt.AlignCenter)
        self.X_field.setPlaceholderText('x') 
        self.SSegment = QLabel(",")
        self.base.addWidget(self.SSegment)
        self.SSegment.setFixedWidth(7)
        self.Y_field = QLineEdit()
        self.base.addWidget(self.Y_field)
        self.Y_field.setFixedWidth(70)
        self.Y_field.setAlignment(Qt.AlignCenter)
        self.Y_field.setPlaceholderText('y') 
        self.TSegment = QLabel(",")
        self.base.addWidget(self.TSegment)
        self.TSegment.setFixedWidth(7)
        self.Z_field = QLineEdit()
        self.base.addWidget(self.Z_field)
        self.Z_field.setAlignment(Qt.AlignCenter)
        self.Z_field.setPlaceholderText('z') 
        self.Z_field.setFixedWidth(70)
        self.FSegment = QLabel(")")
        self.base.addWidget(self.FSegment)
        self.FSegment.setFixedWidth(12)
        self.X_field.textChanged.connect(self.text_changed_x)
        self.Y_field.textChanged.connect(self.text_changed_y)
        self.Z_field.textChanged.connect(self.text_changed_z)

    def text_changed_x(self, text):
        self.x = text

    def text_changed_y(self, text):
        self.y = text

    def text_changed_z(self, text):
        self.z = text

    def set_point(self, point):
        if point.x % 1 == 0:
            self.X_field.setText(str(int(point.x)))
        else:
            self.X_field.setText(str(point.x))

        if point.y % 1 == 0:
            self.Y_field.setText(str(int(point.y)))
        else:
            self.X_field.setText(str(point.y))

        if point.z % 1 == 0:
            self.Z_field.setText(str(int(point.z)))
        else:
            self.Z_field.setText(str(point.z))

        self.point_name_input.set_text(point.primitive_name)

    def get_primitive(self):
        point_name = self.point_name_input.get_text()
        if len(point_name) < 1:
            return None
        
        try:
            point = Point([self.x, self.y, self.z])
            point.build()
            point.primitive_name = point_name
            return point
        except:
            return None