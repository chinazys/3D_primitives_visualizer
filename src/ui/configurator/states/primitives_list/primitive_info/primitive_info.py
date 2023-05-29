from PyQt5.QtWidgets import (QHBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from os import getcwd

from ui.configurator.configurator_types import *
from util.shift_color import shift_color

class PrimitiveInfo:
    """
    This module defines the `PrimitiveInfo` class, which is a widget used to display information about a primitive in the configurator.

    The `PrimitiveInfo` widget displays the primitive type icon, primitive name, and a delete button. It allows the user to toggle the visibility of the primitive, edit its name, and delete it.

    The `PrimitiveInfo` class has the following main components:
    - `button_primitive_type`: QPushButton that displays the primitive type icon and toggles the visibility of the primitive.
    - `button_name`: QPushButton that displays the primitive name and allows the user to edit it.
    - `button_delete`: QPushButton that triggers the deletion of the primitive.

    Usage:
    1. Create an instance of `PrimitiveInfo` by passing the primitive, index, and the `primitives_list` widget.
    2. Add the `PrimitiveInfo` widget to the layout or container where you want to display the primitive information.
    3. Connect the appropriate signals to handle the visibility toggle, name editing, and deletion of the primitive.
    """
    BUTTON_SIZE = 60
    ICON_RELATIVE_SIZE = 0.7

    def __init__(self, primitive, index, primitives_list, top_offset=0):
        self.primitive = primitive
        self.index = index
        self.primitives_list = primitives_list
        self.is_visible = True

        self.base=QHBoxLayout()
        self.base.setSpacing(0)
        self.base.setContentsMargins(0, top_offset, 0, 0)

        self.button_primitive_type = QPushButton()
        self.button_primitive_type.setFixedWidth(self.BUTTON_SIZE)
        self.button_primitive_type.setFixedHeight(self.BUTTON_SIZE)
        self.button_primitive_type.setIcon(QIcon(getcwd() + self.get_icon_relative_path()))
        self.button_primitive_type.setIconSize(QSize(int(self.BUTTON_SIZE * self.ICON_RELATIVE_SIZE), int(self.BUTTON_SIZE * self.ICON_RELATIVE_SIZE)))
        self.button_primitive_type.setStyleSheet(
            "QPushButton{ background-color: " + self.primitive.primitive_color + "; border:2px solid rgb(0, 0, 0); } QPushButton:hover {background-color: " + shift_color(self.primitive.primitive_color) + ";}")
        self.button_primitive_type.clicked.connect(self.primitive_type_button_click)
        self.base.addWidget(self.button_primitive_type)

        self.button_name = QPushButton(self.primitive.primitive_name)
        self.button_name.setFixedHeight(self.BUTTON_SIZE)
        self.button_name.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(230,230,230);}")
        self.button_name.clicked.connect(self.name_button_click)
        self.base.addWidget(self.button_name)
        
        self.button_delete = QPushButton()
        self.button_delete.setFixedWidth(self.BUTTON_SIZE)
        self.button_delete.setFixedHeight(self.BUTTON_SIZE)
        self.button_delete.setIcon(QIcon(getcwd() + "/icons/trash.png"))
        self.button_delete.setIconSize(QSize(int(self.BUTTON_SIZE * self.ICON_RELATIVE_SIZE), int(self.BUTTON_SIZE * self.ICON_RELATIVE_SIZE)))
        self.button_delete.setStyleSheet("QPushButton{background-color: rgb(255,0,0); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(210,0,0);}")
        self.button_delete.clicked.connect(self.delete_button_click)
        self.base.addWidget(self.button_delete)

    def get_icon_relative_path(self):
        if self.primitive.primitive_type == CONFIGURATOR_TYPE_LINE:
            return "/icons/line.png"
        elif self.primitive.primitive_type == CONFIGURATOR_TYPE_CURVE:
            return "/icons/curve.png"
        elif self.primitive.primitive_type == CONFIGURATOR_TYPE_CYLINDRICAL_SURFACE:
            return "/icons/cylinder.png"
        elif self.primitive.primitive_type == CONFIGURATOR_TYPE_CONICAL_SURFACE:
            return "/icons/cone.png"
        elif self.primitive.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
            return "/icons/hyperboloid.png"
        elif self.primitive.primitive_type == CONFIGURATOR_TYPE_PLANE:
            return "/icons/plane.png"
        else:
            raise Exception('Unknown primitive type') 

    def primitive_type_button_click(self):
        self.is_visible = not self.is_visible
        self.primitives_list.configurator.window.on_primitive_visibility_changed(self.index, self.is_visible)
        if self.is_visible:
            self.button_primitive_type.setStyleSheet(
                "QPushButton{ background-color: " + self.primitive.primitive_color + "; border:2px solid rgb(0, 0, 0); } QPushButton:hover {background-color: " + shift_color(self.primitive.primitive_color) + ";}")
        else:
            self.button_primitive_type.setStyleSheet("QPushButton{ background-color: transparent; border:2px solid rgb(0, 0, 0); } QPushButton:hover {background-color: rgb(230,230,230);} ")
        
    def name_button_click(self):
        self.primitives_list.configurator.on_configurator_state_changed(True, primitive=self.primitive, primitive_index=self.index)

    def delete_button_click(self):
        self.primitives_list.on_delete_primitive_button_click(self.index)

