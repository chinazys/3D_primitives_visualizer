from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

HELP_PANEL_LAYOUT_RELATIVE_WIDTH = 50

class SupportedFunctionsScrollable(QScrollArea):
    """
    This module defines the `SupportedFunctionsScrollable` class, which is a scrollable area that displays supported functions and their descriptions.

    The `SupportedFunctionsScrollable` class inherits from `QScrollArea` and has the following main components:
    - `label`: A `QLabel` that displays the text content inside the scrollable area.

    Usage:
    1. Create an instance of `SupportedFunctionsScrollable`.
    2. The scrollable area is populated with text content from the 'docs/help.txt' file.
    """
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        self.setWidgetResizable(True)
 
        content = QWidget(self)
        self.setWidget(content)
 
        layout = QVBoxLayout(content)
 
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)

        layout.addWidget(self.label)
        
        with open('docs/help.txt', 'r') as file:
            help_text = file.read()
        
        self.label.setText(help_text)

class HelpPanel:
    """
    This module defines the `HelpPanel` class, which represents a panel that displays help information.

    The `HelpPanel` class has the following main components:
    - `frame`: An instance of the `QFrame` class, representing the frame that contains the help panel.
    - `vertical_layout`: An instance of the `QVBoxLayout` class, defining the vertical layout of the help panel.
    - `title`: A `QLabel` that displays the title of the help panel.
    - `supported_functions_scrollable`: An instance of the `SupportedFunctionsScrollable` class, which is a scrollable area displaying supported functions and their descriptions.

    Usage:
    1. Create an instance of `HelpPanel` by passing the window widget.
    2. Use the `show` method to display the help panel.
    3. Use the `hide` method to hide the help panel.
    """
    def __init__(self, window):
        self.frame = QFrame()
        
        window.horizontal_layout.addWidget(self.frame, HELP_PANEL_LAYOUT_RELATIVE_WIDTH)
        self.frame.hide()

        self.vertical_layout = QVBoxLayout()

        self.title = QLabel('Help')
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.vertical_layout.addWidget(self.title)
        
        self.supported_functions_scrollable = SupportedFunctionsScrollable()
        self.vertical_layout.addWidget(self.supported_functions_scrollable)

        self.frame.setLayout(self.vertical_layout)
    
    def hide(self):
        self.frame.hide()
    
    def show(self):
        self.frame.show()