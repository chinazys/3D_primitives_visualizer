from PyQt5.QtWidgets import (QLabel, QHBoxLayout,QPushButton)
from PyQt5.QtGui import QIcon,QPixmap
from os import getcwd

class PrimitiveInfo:
    def __init__(self, primitv_type:str, primitiv_name:str, index:int, primitives_list):
        self.index = index
        self.primitives_list = primitives_list

        self.base=QHBoxLayout()
        self.base.setSpacing(0)
        self.icon=QPushButton()
        #self.icon.setPixmap() for image
        self.button_name = QPushButton(primitiv_name)
        self.button_name.clicked.connect(self.name_button_click)
        self.buuton_delete = QPushButton()
        self.base.addWidget(self.icon)
        self.base.addWidget(self.button_name)
        self.base.addWidget(self.buuton_delete)
        self.icon.setFixedWidth(43)
        self.icon.setFixedHeight(43)
        self.icon.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);}")
        self.button_name.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(230,230,230);}")
        self.buuton_delete.setFixedWidth(43)
        self.buuton_delete.setFixedHeight(43)
        self.buuton_delete.setStyleSheet("QPushButton{background-color: rgb(255,0,0); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(210,0,0);}")
        self.buuton_delete.setIcon(QIcon(getcwd() + "/ui/icons/delete.png"))
        self.buuton_delete.clicked.connect(self.delete_buuton_clicl)

    def name_button_click(self):
        print('edit')

    def delete_buuton_clicl(self):
        self.primitives_list.on_delete_primitive_button_click(self.index)

