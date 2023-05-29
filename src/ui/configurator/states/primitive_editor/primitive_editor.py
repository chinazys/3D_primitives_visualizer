from PyQt5.QtWidgets import (QComboBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from ui.configurator.configurator_types import *
from ui.configurator.states.primitive_editor.conical_surface_layout.conical_surface_layout import ConicalSurfaceLayout
from ui.configurator.states.primitive_editor.cylindrical_surface_layout.cylindrical_surface_layout import CylindricalSurfaceLayout
from ui.configurator.states.primitive_editor.line_layout.line_layout import LineLayout
from ui.configurator.states.primitive_editor.plane_layout.plane_layout import PlaneLayout
from ui.configurator.states.primitive_editor.rotational_surface_layout.rotational_surface_layout import RotationalSurfaceLayout
from ui.configurator.separator.separator import PaddedSeparator
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.name_layout.name_layout import NameLayout
from ui.configurator.states.primitive_editor.check_box.check_box import CheckBoxLayout
from ui.configurator.states.primitive_editor.color_opacity_picker.color_opacity_picker import ColorOpacityPicker
from util.clear_qt_layout import clear_qt_layout

class PrimitiveEditor(QWidget):
    """
    This module defines the `PrimitiveEditor` class, which is a PyQt5 widget used for configuring and editing different types of primitives.

    The `PrimitiveEditor` widget provides a user interface for setting various parameters of a primitive, such as its name, color, opacity, flags, and specific parameters based on the selected primitive type. It allows the user to select a primitive type from a dropdown menu (or displays the type label if editing an existing primitive), set the primitive name, choose a color and opacity, enable/disable flags like text and animation, and configure the parameters specific to each primitive type.

    The `PrimitiveEditor` class has the following main components:
    - Top Section: Contains a combo box (QComboBox) for selecting the primitive type.
    - Center Section: Contains layouts for configuring the name, color, flags, and primitive-specific parameters.
    - Bottom Section: Contains buttons for canceling or confirming the changes made to the primitive.

    Usage:
    1. Create an instance of `PrimitiveEditor` by passing the configurator, initial primitive, and initial primitive index (if editing an existing primitive).
    2. Add the `PrimitiveEditor` widget to your application's layout or dialog.
    3. Handle the `on_cancel_button_click` and `on_confirm_button_click` signals to perform actions when the user cancels or confirms the changes.
    4. Retrieve the configured primitive using the `get_primitive()` method.
    """
    def __init__(self, configurator, initial_primitive, initial_primitive_index):
        super().__init__()

        self.configurator = configurator
        self.initial_primitive = initial_primitive
        self.initial_primitive_index = initial_primitive_index
        
        self.vertical_layout = QVBoxLayout()
        
        self.vertical_layout.setContentsMargins(1, 1, 1, 1)

        self.top_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.top_vertical_layout)
        self.top_vertical_layout.setAlignment(Qt.AlignTop)

        self.center_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.center_vertical_layout)
        self.center_vertical_layout.setAlignment(Qt.AlignVCenter)

        self.bottom_vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(self.bottom_vertical_layout)
        self.bottom_vertical_layout.setAlignment(Qt.AlignBottom)

        if self.initial_primitive is None:
            self.primitive_type_selector = QComboBox()
            self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
            self.primitive_type = CONFIGURATOR_TYPES[0]
            self.primitive_type_selector.currentTextChanged.connect(self.on_primitive_type_changed)
            self.top_vertical_layout.addWidget(self.primitive_type_selector)
        else:
            self.primitive_type = self.initial_primitive.primitive_type
            
            self.set_primitive_type_label_layout()
            self.top_vertical_layout.addLayout(self.primitive_type_label_layout)

            self.separator = PaddedSeparator(vertical_padding=8)
            self.top_vertical_layout.addLayout(self.separator.layout)
        
        self.name_layout = NameLayout(None if self.initial_primitive is None else self.initial_primitive.primitive_name)
        self.center_vertical_layout.addLayout(self.name_layout.layout)

        self.color_opacity_picker = ColorOpacityPicker(self.primitive_type == CONFIGURATOR_TYPE_LINE or self.primitive_type == CONFIGURATOR_TYPE_CURVE,
                                                        None if self.initial_primitive is None else self.initial_primitive.primitive_color,
                                                        None if self.initial_primitive is None else self.initial_primitive.primitive_opacity)
        self.center_vertical_layout.addLayout(self.color_opacity_picker.layout)
        
        self.set_flags_layout()
        self.center_vertical_layout.addLayout(self.flags_horizontal_layout)

        self.set_primitive_layout(self.initial_primitive)
        self.center_vertical_layout.addLayout(self.primitive_vertical_layout)

        self.set_bottom_buttons_layout()
        self.bottom_vertical_layout.addLayout(self.bottom_horizontal_layout)
    
    def set_primitive_type_label_layout(self):
        self.primitive_type_label_layout = QHBoxLayout()
        self.primitive_type_label = QLabel(self.primitive_type)
        self.primitive_type_label.setContentsMargins(0, 6, 0, 0)
        self.primitive_type_label.setFont(QFont('Arial', 20))
        self.primitive_type_label_layout.addWidget(self.primitive_type_label)     
        self.primitive_type_label_layout.setAlignment(Qt.AlignCenter)

    def set_bottom_buttons_layout(self):  
        self.bottom_horizontal_layout = QHBoxLayout()

        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.setToolTip('Click to go back')
        self.cancel_button.clicked.connect(self.on_cancel_button_click)
        self.bottom_horizontal_layout.addWidget(self.cancel_button)
        
        self.confirm_button = QPushButton('Confirm', self)
        self.confirm_button.setToolTip('Click to plot')
        self.confirm_button.clicked.connect(self.on_confirm_button_click)
        self.bottom_horizontal_layout.addWidget(self.confirm_button)

    def set_primitive_layout(self, primitive=None):
        self.primitive_vertical_layout = QVBoxLayout()

        self.separator = PaddedSeparator()
        self.primitive_vertical_layout.addLayout(self.separator.layout)

        if self.primitive_type == CONFIGURATOR_TYPE_LINE:
            self.primitive_layout = LineLayout(self.initial_primitive)
        elif self.primitive_type == CONFIGURATOR_TYPE_CURVE:
            self.primitive_layout = CurveLayout(self.initial_primitive, curve_label=None)
        elif self.primitive_type == CONFIGURATOR_TYPE_CYLINDRICAL_SURFACE:
            self.primitive_layout = CylindricalSurfaceLayout(self.initial_primitive)
        elif self.primitive_type == CONFIGURATOR_TYPE_CONICAL_SURFACE:
            self.primitive_layout = ConicalSurfaceLayout(self.initial_primitive)
        elif self.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
            self.primitive_layout = RotationalSurfaceLayout(self.initial_primitive)
        elif self.primitive_type == CONFIGURATOR_TYPE_PLANE:
            self.primitive_layout = PlaneLayout(self.initial_primitive)
        else:
            raise Exception('Unknown primitive type')   
             
        self.primitive_vertical_layout.addLayout(self.primitive_layout.layout)

    def set_flags_layout(self):
        self.flags_horizontal_layout = QHBoxLayout()

        self.flag_text_check_box_layout = CheckBoxLayout("Enable labels  ")
        self.flags_horizontal_layout.addLayout(self.flag_text_check_box_layout.base)

        self.flag_animation_check_box_layout = CheckBoxLayout("Enable animation")
        if not (self.primitive_type == CONFIGURATOR_TYPE_LINE or self.primitive_type == CONFIGURATOR_TYPE_CURVE): 
            self.flags_horizontal_layout.addLayout(self.flag_animation_check_box_layout.base)

        if not self.initial_primitive is None:
            self.flag_text_check_box_layout.set_state(self.initial_primitive.flag_text)
            self.flag_animation_check_box_layout.set_state(self.initial_primitive.flag_animation)        

    def on_primitive_type_changed(self, primitive_type):
        self.primitive_type = primitive_type

        clear_qt_layout(self.color_opacity_picker.layout)
        clear_qt_layout(self.primitive_vertical_layout)
        clear_qt_layout(self.flags_horizontal_layout)

        self.color_opacity_picker = ColorOpacityPicker(self.primitive_type == CONFIGURATOR_TYPE_LINE or self.primitive_type == CONFIGURATOR_TYPE_CURVE)
        self.center_vertical_layout.addLayout(self.color_opacity_picker.layout)

        self.set_flags_layout()
        self.center_vertical_layout.addLayout(self.flags_horizontal_layout)

        self.set_primitive_layout()
        self.center_vertical_layout.addLayout(self.primitive_vertical_layout)
        
    @pyqtSlot()
    def on_cancel_button_click(self):
        self.configurator.on_configurator_state_changed(False)
    
    @pyqtSlot()
    def on_confirm_button_click(self):
        primitive_name = self.name_layout.get_name()
        if primitive_name is None:
            self.configurator.window.show_error('Primitive Name Error', 'Primitive name was not set correctly. Please fill the corresponding field and try again.')
            return
        
        primitive = self.primitive_layout.get_primitive()
        if primitive is None:
            self.configurator.window.show_error('Input Error', 'Primitive parameters were not set correctly. Please re-check your input and try again.')
            return
        
        primitive.primitive_name = primitive_name
        primitive.primitive_type = self.primitive_type
        primitive.primitive_color = self.color_opacity_picker.get_color_hex()
        primitive.primitive_opacity = self.color_opacity_picker.get_opacity()
        primitive.flag_text = self.flag_text_check_box_layout.get_state()
        primitive.flag_animation = self.flag_animation_check_box_layout.get_state()

        try:
            if self.initial_primitive is None:
                self.configurator.window.on_primitive_added(primitive)
            else:
                self.configurator.window.on_primitive_edited(primitive, self.initial_primitive_index)
        except:
            self.configurator.window.show_error('Plotting Error', 'Primitive with the given parameters can not be plotted. Please re-check your input and try again.')
        
        self.configurator.on_configurator_state_changed(False)