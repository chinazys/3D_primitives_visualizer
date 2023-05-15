from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QLabel, QLineEdit)
import numpy as np

from ui.configurator.states.primitive_editor.color_opacity_picker.vcolorpicker.vcolorpicker import getColor, useAlpha, rgb2hex, useLightTheme

class ColorOpacityPicker:
    DEFAULT_LINE_OPACITY = 100
    DEFAULT_SURFACE_OPACITY = 50

    def __init__(self, line_or_curve=False):
        self.color_opacity = list(np.random.choice(range(256), size=3))
        if line_or_curve:
            self.color_opacity.append(self.DEFAULT_LINE_OPACITY)
        else:
            self.color_opacity.append(self.DEFAULT_SURFACE_OPACITY)
            
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
        print(self.get_color_hex(), self.get_opacity())
