from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QLabel, QLineEdit)
import numpy as np

from ui.configurator.states.primitive_editor.color_opacity_picker.vcolorpicker.vcolorpicker import getColor, useAlpha, rgb2hex, hex2rgb, useLightTheme

class ColorOpacityPicker:
    """A color and opacity picker widget.

    - Constants:
        - DEFAULT_LINE_OPACITY: The default opacity value for lines or curves.
        - DEFAULT_SURFACE_OPACITY: The default opacity value for surfaces.

    - Attributes:
        - color_opacity (list): The list representing the color and opacity values.
        - layout (QHBoxLayout): The layout for the color opacity picker widget.
        - color_label (QLabel): The label for the color and opacity.
        - color_button (QPushButton): The button for changing the color and opacity.

    - Methods:
        - __init__(line_or_curve, initial_color=None, initial_opacity=None): Initialize a ColorOpacityPicker object.
        - get_color_hex() -> str: Get the color in hexadecimal format.
        - get_opacity() -> float: Get the opacity value.
        - _update_color_button_style(): Update the style of the color button.
        - _button_color_click(): Handle the button click event for changing the color and opacity.

    """
    
    DEFAULT_LINE_OPACITY = 100
    DEFAULT_SURFACE_OPACITY = 50

    def __init__(self, line_or_curve, initial_color=None, initial_opacity=None):
        if initial_color is None:
            self.color_opacity = list(np.random.choice(range(256), size=3))
        else:
            rgb_tuple = hex2rgb(initial_color[1:])
            self.color_opacity = [int(c) for c in rgb_tuple]
        
        if initial_opacity is None:
            if line_or_curve:
                self.color_opacity.append(self.DEFAULT_LINE_OPACITY)
            else:
                self.color_opacity.append(self.DEFAULT_SURFACE_OPACITY)
        else:
            self.color_opacity.append(int(initial_opacity * 100))
            
        useAlpha(True)
        # useLightTheme(True)

        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)

        self.color_label = QLabel('Color & Opacity:  ')
        self.layout.addWidget(self.color_label)
        
        self.color_button = QPushButton()
        self.color_button.clicked.connect(self._button_color_click)
        
        self._update_color_button_style()

        self.color_button.setToolTip('Click to change color & opacity')
        self.layout.addWidget(self.color_button)

    def get_color_hex(self):
        return '#' + rgb2hex((self.color_opacity[0], self.color_opacity[1], self.color_opacity[2]))

    def get_opacity(self):
        return self.color_opacity[3] / 100

    def _update_color_button_style(self):
        self.color_button.setStyleSheet("QPushButton{background-color:" + "rgba(" + str(self.color_opacity[0]) + ', ' + str(self.color_opacity[1]) + ', ' + str(self.color_opacity[2]) +  ', ' + str(self.color_opacity[3]) +  "%); margin:0px; border:2px solid rgb(0, 0, 0);}")

    def _button_color_click(self):
        color_opacity = getColor(self.color_opacity)
        if len(color_opacity) == 3:
           return
        self.color_opacity = color_opacity 
        self._update_color_button_style()