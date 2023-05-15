# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dark_alpha.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(400, 333)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorPicker.sizePolicy().hasHeightForWidth())
        ColorPicker.setSizePolicy(sizePolicy)
        ColorPicker.setMinimumSize(QtCore.QSize(400, 333))
        ColorPicker.setMaximumSize(QtCore.QSize(400, 333))
        ColorPicker.setStyleSheet("QWidget{\n"
"    background-color: none;\n"
"}\n"
"\n"
"/*  LINE EDIT */\n"
"QLineEdit{\n"
"    color: rgb(221, 221, 221);\n"
"    background-color: #303030;\n"
"    border: 2px solid #303030;\n"
"    border-radius: 5px;\n"
"    selection-color: rgb(16, 16, 16);\n"
"    selection-background-color: rgb(221, 51, 34);\n"
"    font-family: Segoe UI;\n"
"    font-size: 11pt;\n"
"}\n"
"QLineEdit::focus{\n"
"    border-color: #aaaaaa;\n"
"}\n"
"\n"
"/* PUSH BUTTON */\n"
"QPushButton{\n"
"    border: 2px solid #aaa;\n"
"    border-radius: 5px;\n"
"    font-family: Segoe UI;\n"
"    font-size: 9pt;\n"
"    font-weight: bold;\n"
"    color: #ccc;\n"
"    width: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid #aaa;\n"
"    color: #222;\n"
"    background-color: #aaa;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #aaa;\n"
"    color: #222;\n"
"    background-color: #aaa;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ColorPicker)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drop_shadow_frame = QtWidgets.QFrame(ColorPicker)
        self.drop_shadow_frame.setStyleSheet("QFrame{\n"
"background-color: #202020;\n"
"border-radius: 10px;\n"
"}")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 32))
        self.title_bar.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(16, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.window_title = QtWidgets.QLabel(self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_title.sizePolicy().hasHeightForWidth())
        self.window_title.setSizePolicy(sizePolicy)
        self.window_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.window_title.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"    font-family: Segoe UI;\n"
"    font-size: 9pt;\n"
"}")
        self.window_title.setAlignment(QtCore.Qt.AlignCenter)
        self.window_title.setObjectName("window_title")
        self.horizontalLayout_2.addWidget(self.window_title)
        self.exit_btn = QtWidgets.QPushButton(self.title_bar)
        self.exit_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.exit_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.exit_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: #aaaaaa;\n"
"    border-radius: 8px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #666666;\n"
"}")
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(12, 12))
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_2.addWidget(self.exit_btn)
        self.verticalLayout_3.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.content_bar.setStyleSheet("QWidget{\n"
"border-radius: 5px\n"
"}\n"
"#color_view{\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}\n"
"#black_overlay{\n"
"    border-bottom-left-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_bar)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color_view = QtWidgets.QFrame(self.content_bar)
        self.color_view.setMinimumSize(QtCore.QSize(200, 200))
        self.color_view.setMaximumSize(QtCore.QSize(200, 200))
        self.color_view.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: qlineargradient(x1:1, x2:0, stop:0 hsl(0%,100%,50%), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.color_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_view.setObjectName("color_view")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.color_view)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.black_overlay = QtWidgets.QFrame(self.color_view)
        self.black_overlay.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"\n"
"")
        self.black_overlay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.black_overlay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.black_overlay.setObjectName("black_overlay")
        self.selector = QtWidgets.QFrame(self.black_overlay)
        self.selector.setGeometry(QtCore.QRect(194, 20, 12, 12))
        self.selector.setMinimumSize(QtCore.QSize(12, 12))
        self.selector.setMaximumSize(QtCore.QSize(12, 12))
        self.selector.setStyleSheet("background-color:none;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.selector.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selector.setObjectName("selector")
        self.black_ring = QtWidgets.QLabel(self.selector)
        self.black_ring.setGeometry(QtCore.QRect(1, 1, 10, 10))
        self.black_ring.setMinimumSize(QtCore.QSize(10, 10))
        self.black_ring.setMaximumSize(QtCore.QSize(10, 10))
        self.black_ring.setBaseSize(QtCore.QSize(10, 10))
        self.black_ring.setStyleSheet("background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 5px;")
        self.black_ring.setText("")
        self.black_ring.setObjectName("black_ring")
        self.verticalLayout_2.addWidget(self.black_overlay)
        self.horizontalLayout.addWidget(self.color_view)
        self.frame_2 = QtWidgets.QFrame(self.content_bar)
        self.frame_2.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hue_bg = QtWidgets.QFrame(self.frame_2)
        self.hue_bg.setGeometry(QtCore.QRect(10, 0, 20, 200))
        self.hue_bg.setMinimumSize(QtCore.QSize(20, 200))
        self.hue_bg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 5px;")
        self.hue_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hue_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hue_bg.setObjectName("hue_bg")
        self.hue_selector = QtWidgets.QLabel(self.frame_2)
        self.hue_selector.setGeometry(QtCore.QRect(7, 185, 26, 15))
        self.hue_selector.setMinimumSize(QtCore.QSize(26, 0))
        self.hue_selector.setStyleSheet("background-color: #aaa;\n"
"border-radius: 5px;")
        self.hue_selector.setText("")
        self.hue_selector.setObjectName("hue_selector")
        self.hue = QtWidgets.QFrame(self.frame_2)
        self.hue.setGeometry(QtCore.QRect(7, 0, 26, 200))
        self.hue.setMinimumSize(QtCore.QSize(20, 200))
        self.hue.setStyleSheet("background-color: none;")
        self.hue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hue.setObjectName("hue")
        self.horizontalLayout.addWidget(self.frame_2)
        self.editfields = QtWidgets.QFrame(self.content_bar)
        self.editfields.setMinimumSize(QtCore.QSize(110, 200))
        self.editfields.setMaximumSize(QtCore.QSize(120, 200))
        self.editfields.setStyleSheet("QLabel{\n"
"    font-family: Segoe UI;\n"
"font-weight: bold;\n"
"    font-size: 11pt;\n"
"    color: #aaaaaa;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.editfields.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editfields.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editfields.setObjectName("editfields")
        self.formLayout = QtWidgets.QFormLayout(self.editfields)
        self.formLayout.setContentsMargins(15, 0, 15, 1)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.color_vis = QtWidgets.QLabel(self.editfields)
        self.color_vis.setMinimumSize(QtCore.QSize(0, 24))
        self.color_vis.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.color_vis.setText("")
        self.color_vis.setObjectName("color_vis")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_vis)
        self.lastcolor_vis = QtWidgets.QLabel(self.editfields)
        self.lastcolor_vis.setMinimumSize(QtCore.QSize(0, 24))
        self.lastcolor_vis.setStyleSheet("/* ALL CHANGES HERE WILL BE OVERWRITTEN */;\n"
"background-color: rgb(0, 0, 0);")
        self.lastcolor_vis.setText("")
        self.lastcolor_vis.setObjectName("lastcolor_vis")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastcolor_vis)
        self.lbl_red = QtWidgets.QLabel(self.editfields)
        self.lbl_red.setObjectName("lbl_red")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_red)
        self.red = QtWidgets.QLineEdit(self.editfields)
        self.red.setAlignment(QtCore.Qt.AlignCenter)
        self.red.setClearButtonEnabled(False)
        self.red.setObjectName("red")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.red)
        self.lbl_green = QtWidgets.QLabel(self.editfields)
        self.lbl_green.setObjectName("lbl_green")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_green)
        self.green = QtWidgets.QLineEdit(self.editfields)
        self.green.setAlignment(QtCore.Qt.AlignCenter)
        self.green.setObjectName("green")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.green)
        self.lbl_blue = QtWidgets.QLabel(self.editfields)
        self.lbl_blue.setObjectName("lbl_blue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_blue)
        self.blue = QtWidgets.QLineEdit(self.editfields)
        self.blue.setAlignment(QtCore.Qt.AlignCenter)
        self.blue.setObjectName("blue")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.blue)
        self.lbl_hex = QtWidgets.QLabel(self.editfields)
        self.lbl_hex.setStyleSheet("font-size: 14pt;")
        self.lbl_hex.setObjectName("lbl_hex")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_hex)
        self.hex = QtWidgets.QLineEdit(self.editfields)
        self.hex.setAlignment(QtCore.Qt.AlignCenter)
        self.hex.setObjectName("hex")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.hex)
        self.lbl_alpha = QtWidgets.QLabel(self.editfields)
        self.lbl_alpha.setObjectName("lbl_alpha")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_alpha)
        self.alpha = QtWidgets.QLineEdit(self.editfields)
        self.alpha.setAlignment(QtCore.Qt.AlignCenter)
        self.alpha.setObjectName("alpha")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.alpha)
        self.horizontalLayout.addWidget(self.editfields)
        self.verticalLayout_3.addWidget(self.content_bar)
        self.button_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bar.sizePolicy().hasHeightForWidth())
        self.button_bar.setSizePolicy(sizePolicy)
        self.button_bar.setStyleSheet("QFrame{\n"
"background-color: #1d1d1d;\n"
"padding: 5px\n"
"}\n"
"")
        self.button_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_bar.setObjectName("button_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.button_bar)
        self.horizontalLayout_3.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.button_bar)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_3.addWidget(self.button_bar)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
        self.lbl_red.setBuddy(self.red)
        self.lbl_green.setBuddy(self.green)
        self.lbl_blue.setBuddy(self.blue)
        self.lbl_hex.setBuddy(self.blue)
        self.lbl_alpha.setBuddy(self.blue)

        self.retranslateUi(ColorPicker)
        QtCore.QMetaObject.connectSlotsByName(ColorPicker)
        ColorPicker.setTabOrder(self.red, self.green)
        ColorPicker.setTabOrder(self.green, self.blue)

    def retranslateUi(self, ColorPicker):
        _translate = QtCore.QCoreApplication.translate
        ColorPicker.setWindowTitle(_translate("ColorPicker", "Form"))
        self.window_title.setText(_translate("ColorPicker", "<strong>Color Picker</strong>"))
        self.lbl_red.setText(_translate("ColorPicker", "R"))
        self.red.setText(_translate("ColorPicker", "255"))
        self.lbl_green.setText(_translate("ColorPicker", "G"))
        self.green.setText(_translate("ColorPicker", "255"))
        self.lbl_blue.setText(_translate("ColorPicker", "B"))
        self.blue.setText(_translate("ColorPicker", "255"))
        self.lbl_hex.setText(_translate("ColorPicker", "#"))
        self.hex.setText(_translate("ColorPicker", "ffffff"))
        self.lbl_alpha.setText(_translate("ColorPicker", "A"))
        self.alpha.setText(_translate("ColorPicker", "100"))
