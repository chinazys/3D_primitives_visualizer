from PyQt5.QtWidgets import (QHBoxLayout,QPushButton)
from PyQt5.QtGui import QIcon
from os import getcwd

from ui.configurator.configurator_types import *

class PrimitiveInfo:
    ICON_SIZE = 43

    def __init__(self, primitive_type:str, primitive_name:str, index:int, primitives_list):
        self.primitive_type = primitive_type
        self.primitive_name = primitive_name
        self.index = index
        self.primitives_list = primitives_list

        self.base=QHBoxLayout()
        self.base.setSpacing(0)
        
        self.button_primitive_type = QPushButton()
        self.button_primitive_type.setFixedWidth(self.ICON_SIZE)
        self.button_primitive_type.setFixedHeight(self.ICON_SIZE)
        self.button_primitive_type.setStyleSheet("QPushButton{ background-color: rgb(255,255,255); border:2px solid rgb(0, 0, 0); }")
        self.button_primitive_type.setIcon(QIcon(getcwd() + self.get_icon_relative_path()))
        self.button_primitive_type.clicked.connect(self.primitive_type_button_click)
        self.base.addWidget(self.button_primitive_type)

        self.button_name = QPushButton(primitive_name)
        self.button_name.clicked.connect(self.name_button_click)
        self.button_name.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(230,230,230);}")
        self.base.addWidget(self.button_name)
        
        self.button_delete = QPushButton()
        self.button_delete.setFixedWidth(self.ICON_SIZE)
        self.button_delete.setFixedHeight(self.ICON_SIZE)
        self.button_delete.setStyleSheet("QPushButton{background-color: rgb(255,0,0); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(210,0,0);}")
        self.button_delete.setIcon(QIcon(getcwd() + "/src/ui/icons/delete.png"))
        self.button_delete.clicked.connect(self.delete_button_click)
        self.base.addWidget(self.button_delete)

    def get_icon_relative_path(self):
        if self.primitive_type == CONFIGURATOR_TYPE_LINE:
            return "/src/ui/icons/line.png"
        elif self.primitive_type == CONFIGURATOR_TYPE_CURVE:
            return "/src/ui/icons/curve.png"
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEMOVE:
            return "/src/ui/icons/cylinder.png"
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE:
            return "/src/ui/icons/cone.png"
        elif self.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
            return "/src/ui/icons/hyperboloid.png"
        elif self.primitive_type == CONFIGURATOR_TYPE_PLANE:
            return "/src/ui/icons/plane.png"
        else:
            raise Exception('Unknown primitive type') 

    def primitive_type_button_click(self):
        print('toggle visibility')

    def name_button_click(self):
        print('edit')

    def delete_button_click(self):
        self.primitives_list.on_delete_primitive_button_click(self.index)

