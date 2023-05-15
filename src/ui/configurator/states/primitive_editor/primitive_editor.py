from PyQt5.QtWidgets import (QComboBox, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from ui.configurator.configurator_types import *
from ui.configurator.states.primitive_editor.conical_surface_layout.conical_surface_layout import ConicalSurfaceLayout
from ui.configurator.states.primitive_editor.cylindrical_surface_layout.cylindrical_surface_layout import CylindricalSurfaceLayout
from ui.configurator.states.primitive_editor.line_layout.line_layout import LineLayout
from ui.configurator.states.primitive_editor.plane_layout.plane_layout import PlaneLayout
from ui.configurator.states.primitive_editor.rotational_surface_layout.rotational_surface_layout import RotationalSurfaceLayout
from ui.configurator.states.primitive_editor.separator.separator import PaddedSeparator
from ui.configurator.states.primitive_editor.point_layout.point_layout import PointLayout
from ui.configurator.states.primitive_editor.curve_layout.curve_layout import CurveLayout
from ui.configurator.states.primitive_editor.name_layout.name_layout import NameLayout
from ui.configurator.states.primitive_editor.check_box.check_box import CheckBoxLayout
from ui.configurator.states.primitive_editor.color_opacity_picker.color_opacity_picker import ColorOpacityPicker
from primitives.line.line import Line
from primitives.curve.curve import Curve
from primitives.lineMove.lineMove import curve_line
from primitives.lineFixedMove.lineFixedMove import lineFixedMove
# from primitives.linesByCurve.lineByCurve import LineByCurve
from primitives.rotate_surface.rotate_surface import rotate_surface
from primitives.plane.plane import Plane
from util.clear_qt_layout import clear_qt_layout

class PrimitiveEditor(QWidget):
    def __init__(self, configurator):
        super().__init__()

        self.configurator = configurator
        
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

        self.primitive_type_selector = QComboBox()
        self.primitive_type_selector.addItems(CONFIGURATOR_TYPES)
        self.primitive_type = CONFIGURATOR_TYPES[0]
        self.primitive_type_selector.currentTextChanged.connect(self.on_primitive_type_changed)
        self.top_vertical_layout.addWidget(self.primitive_type_selector)
        
        self.name_layout = NameLayout()
        self.center_vertical_layout.addLayout(self.name_layout.layout)

        self.color_opacity_picker = ColorOpacityPicker(line_or_curve=(self.primitive_type == CONFIGURATOR_TYPE_LINE or self.primitive_type == CONFIGURATOR_TYPE_CURVE))
        self.center_vertical_layout.addLayout(self.color_opacity_picker.layout)
        
        self.set_flags_layout()
        self.center_vertical_layout.addLayout(self.flags_horizontal_layout)

        self.set_primitive_layout()
        self.center_vertical_layout.addLayout(self.primitive_vertical_layout)

        self.set_bottom_buttons_layout()
        self.bottom_vertical_layout.addLayout(self.bottom_horizontal_layout)
        
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

    def set_primitive_layout(self):
        self.primitive_vertical_layout = QVBoxLayout()

        self.separator = PaddedSeparator()
        self.primitive_vertical_layout.addLayout(self.separator.layout)

        if self.primitive_type == CONFIGURATOR_TYPE_LINE:
            self.primitive_layout = LineLayout()
        elif self.primitive_type == CONFIGURATOR_TYPE_CURVE:
            self.primitive_layout = CurveLayout(curve_id=None)
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEMOVE:
            self.primitive_layout = CylindricalSurfaceLayout()
        elif self.primitive_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE:
            self.primitive_layout = ConicalSurfaceLayout()
        elif self.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
            self.primitive_layout = RotationalSurfaceLayout()
        elif self.primitive_type == CONFIGURATOR_TYPE_PLANE:
            self.primitive_layout = PlaneLayout()
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

    def on_primitive_type_changed(self, primitive_type):
        self.primitive_type = primitive_type

        clear_qt_layout(self.color_opacity_picker.layout)
        clear_qt_layout(self.primitive_vertical_layout)
        clear_qt_layout(self.flags_horizontal_layout)

        self.color_opacity_picker = ColorOpacityPicker(line_or_curve=(self.primitive_type == CONFIGURATOR_TYPE_LINE or self.primitive_type == CONFIGURATOR_TYPE_CURVE))
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
        
        # if self.primitive_type == CONFIGURATOR_TYPE_LINE:
        #     primitive = Line([(0, 0, 0), (10, 10, 10)])
        # elif self.primitive_type == CONFIGURATOR_TYPE_CURVE:
        #     primitive = Curve(['(t^2 + 1) * sin(t)', '(t^2 + 1) * cos(t)', 't', '-4', '12', '100'])
        # elif self.primitive_type == CONFIGURATOR_TYPE_LINEMOVE:
        #     curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
        #     primitive = curve_line(curve, [1, 0.8414709848078965, 5], [1, 1, 1])
        # # elif self.primitive_type == CONFIGURATOR_TYPE_LINEBYCURVE:
        # #     curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
        # #     line = Line([(-0.5, -0.5, -0.5), [0.5, 0.5, 0.5]])
        # #     primitive = LineByCurve(curve,line)
        # elif self.primitive_type == CONFIGURATOR_TYPE_LINEFIXEDMOVE:
        #     curve = Curve(['50*cos(t)', '50*sin(t)', '-20', '0', '6.29', '100'])
        #     primitive = lineFixedMove(curve, [0,0,100])
        # elif self.primitive_type == CONFIGURATOR_TYPE_ROTATE_SURFACE:
        #     curve = Curve(['t', 'sin(t)', '5', '1', '10', '100'])
        #     primitive = rotate_surface(curve, [1, 0.8414709848078965, 5], [1, 1, 1])
        # elif self.primitive_type == CONFIGURATOR_TYPE_PLANE:
        #     primitive = Plane((5, 2, 30), (10, 10, 50))
        # else:
        #     raise Exception('Unknown primitive type')

        primitive.primitive_name = primitive_name
        primitive.primitive_type = self.primitive_type
        primitive.primitive_color = self.color_opacity_picker.get_color_hex()
        primitive.primitive_opacity = self.color_opacity_picker.get_opacity()
        primitive.flag_text = self.flag_text_check_box_layout.check_box.isChecked()
        primitive.flag_animation = self.flag_animation_check_box_layout.check_box.isChecked()

        try:
            self.configurator.window.on_primitive_added(primitive)
            self.configurator.on_configurator_state_changed(False)
        except:
            self.configurator.window.show_error('Plotting Error', 'Primitive with the given parameters can not be plotted. Please re-check your input and try again.')