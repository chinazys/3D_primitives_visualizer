from PyQt5.QtWidgets import (QLabel, QHBoxLayout, QLineEdit)

class PointTextField:
    def __init__(self, window ,point_letter="A"):
        self.base = QHBoxLayout()
        self.base.setSpacing(0)
        self.FSegment=QLabel(point_letter+"=(")
        self.base.addWidget(self.FSegment)
        self.FSegment.setFixedWidth(40)
        self.x=None; self.y=None; self.z=None
        self.X_field=QLineEdit()
        self.base.addWidget(self.X_field)
        self.X_field.setFixedWidth(70)
        self.SSegment = QLabel(",")
        self.base.addWidget(self.SSegment)
        self.SSegment.setFixedWidth(5)
        self.Y_field = QLineEdit()
        self.base.addWidget(self.Y_field)
        self.Y_field.setFixedWidth(70)
        self.TSegment = QLabel(",")
        self.base.addWidget(self.TSegment)
        self.TSegment.setFixedWidth(5)
        self.Z_field = QLineEdit()
        self.base.addWidget(self.Z_field)
        self.Z_field.setFixedWidth(70)
        self.FSegment = QLabel(")")
        self.base.addWidget(self.FSegment)
        self.FSegment.setFixedWidth(10)
        window.vertical_layout.addLayout(self.base)
        self.X_field.textChanged.connect(self.text_changed_x)
        self.Y_field.textChanged.connect(self.text_changed_y)
        self.Z_field.textChanged.connect(self.text_changed_z)

    def text_changed_x(self,text):
        self.x=text

    def text_changed_y(self,text):
        self.y=text

    def text_changed_z(self,text):
        self.z=text

    def get_values(self):
        values=[self.x,self.y,self.z]
        if values[0]==None or values[1]==None or values[2]==None:
            return False, values
        else:
            return True, values