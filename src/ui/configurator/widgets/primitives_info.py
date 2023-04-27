from PyQt5.QtWidgets import (QLabel, QHBoxLayout,QPushButton)
from PyQt5.QtGui import QIcon,QPixmap
from os import getcwd

class PrimitivInfo:
    def __init__(self, window, primitv_type:str="test_type",primitiv_name:str="test"):
        self.base=QHBoxLayout()
        self.base.setSpacing(0)
        self.icon=QPushButton()
        #self.icon.setPixmap() for image
        self.name = QLabel(primitiv_name)
        self.buuton_create = QPushButton()
        self.buuton_delete = QPushButton()
        self.base.addWidget(self.icon)
        self.base.addWidget(self.name)
        self.base.addWidget(self.buuton_create)
        self.base.addWidget(self.buuton_delete)
        self.icon.setFixedWidth(32)
        self.icon.setFixedHeight(34)
        self.icon.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);}")
        self.name.setStyleSheet("background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0); ")
        self.buuton_create.setFixedWidth(32)
        self.buuton_create.setFixedHeight(34)
        self.buuton_create.setStyleSheet("QPushButton{background-color: rgb(255,255,255); margin:0px; border:2px solid rgb(0, 0, 0);}QPushButton:hover {background-color: rgb(210,210,210);}")
        self.buuton_delete.setFixedWidth(32)
        self.buuton_delete.setFixedHeight(34)
        self.buuton_delete.setStyleSheet("QPushButton{background-color: rgb(255,0,0); margin:0px; border:2px solid rgb(0, 0, 0);} QPushButton:hover {background-color: rgb(210,0,0);}")
        self.icon.setIcon(QIcon(getcwd() + "/ui/icons/edit.png"))
        self.buuton_create.setIcon(QIcon(getcwd() + "/ui/icons/edit.png"))
        self.buuton_delete.setIcon(QIcon(getcwd() + "/ui/icons/delete.png"))
        self.buuton_create.clicked.connect(self.create_buuton_click)
        self.buuton_delete.clicked.connect(self.delete_buuton_clicl)
        window.vertical_layout.addLayout(self.base)

    def create_buuton_click(self):
        print("create")

    def delete_buuton_clicl(self):
        pass

