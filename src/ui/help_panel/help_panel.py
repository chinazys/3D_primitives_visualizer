from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

HELP_PANEL_LAYOUT_RELATIVE_WIDTH = 50

class SupportedFunctionsScrollable(QScrollArea):
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
        
        with open('src/ui/help_panel/help.txt', 'r') as file:
            help_text = file.read()
        
        self.label.setText(help_text)

class HelpPanel:
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