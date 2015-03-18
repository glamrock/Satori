# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Mon Mar 16 22:23:46 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(644, 505)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainForm.setFont(font)
        MainForm.setAutoFillBackground(True)
        MainForm.setStyleSheet("")
        MainForm.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_2 = QtGui.QVBoxLayout(MainForm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(MainForm)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget {\n"
"    background-image: url(:/images/background.png);\n"
"}")
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtGui.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.MainPage)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.software_label = QtGui.QLabel(self.MainPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.software_label.setFont(font)
        self.software_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}\n"
"QLabel::hover {\n"
"    color:rgb(220, 220, 220);\n"
"    bottom:2px;\n"
"}")
        self.software_label.setObjectName("software_label")
        self.horizontalLayout_2.addWidget(self.software_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bridges_label = QtGui.QLabel(self.MainPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.bridges_label.setFont(font)
        self.bridges_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}\n"
"QLabel::hover {\n"
"    color:rgb(220, 220, 220);\n"
"}")
        self.bridges_label.setObjectName("bridges_label")
        self.horizontalLayout.addWidget(self.bridges_label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verify_label = QtGui.QLabel(self.MainPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(24)
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.verify_label.setFont(font)
        self.verify_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}\n"
"QLabel::hover {\n"
"    color:rgb(220, 220, 220);\n"
"}")
        self.verify_label.setObjectName("verify_label")
        self.verticalLayout.addWidget(self.verify_label)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.language_switch = QtGui.QComboBox(self.MainPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_switch.sizePolicy().hasHeightForWidth())
        self.language_switch.setSizePolicy(sizePolicy)
        self.language_switch.setMinimumSize(QtCore.QSize(101, 25))
        self.language_switch.setMaximumSize(QtCore.QSize(90, 30))
        self.language_switch.setStyleSheet("QComboBox  {\n"
"    border: 1px solid #b58dab;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background-color: #ae83a5;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
" \n"
"QComboBox:editable  {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable  {\n"
"\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on  {\n"
"\n"
"}\n"
" \n"
"QComboBox:on  { /* shift the text when the popup opens */\n"
"\n"
"}\n"
" \n"
"QComboBox::drop-down  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    padding-right: 10px;\n"
"    width: 12px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow  {\n"
"    image: url(:/icons/dropdown.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on  { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"}")
        self.language_switch.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.language_switch.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.language_switch.setFrame(True)
        self.language_switch.setObjectName("language_switch")
        self.language_switch.addItem("")
        self.language_switch.addItem("")
        self.horizontalLayout_4.addWidget(self.language_switch)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.setStretch(0, 1)
        self.stackedWidget.addWidget(self.MainPage)
        self.SoftwarePage = QtGui.QWidget()
        self.SoftwarePage.setObjectName("SoftwarePage")
        self.gridLayout = QtGui.QGridLayout(self.SoftwarePage)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, 10, -1, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.software_scrollarea = QtGui.QScrollArea(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.software_scrollarea.sizePolicy().hasHeightForWidth())
        self.software_scrollarea.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.software_scrollarea.setPalette(palette)
        self.software_scrollarea.setAutoFillBackground(True)
        self.software_scrollarea.setStyleSheet("background-color:rgba(142, 116, 173, 60);")
        self.software_scrollarea.setFrameShape(QtGui.QFrame.NoFrame)
        self.software_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.software_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.software_scrollarea.setWidgetResizable(True)
        self.software_scrollarea.setObjectName("software_scrollarea")
        self.software_scrollarea_widgetcontents = QtGui.QWidget()
        self.software_scrollarea_widgetcontents.setGeometry(QtCore.QRect(0, 0, 469, 485))
        self.software_scrollarea_widgetcontents.setObjectName("software_scrollarea_widgetcontents")
        self.software_scrollarea.setWidget(self.software_scrollarea_widgetcontents)
        self.verticalLayout_7.addWidget(self.software_scrollarea)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtGui.QSpacerItem(10, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verify_right_menu_button = QtGui.QPushButton(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verify_right_menu_button.sizePolicy().hasHeightForWidth())
        self.verify_right_menu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.verify_right_menu_button.setFont(font)
        self.verify_right_menu_button.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.verify_right_menu_button.setFlat(False)
        self.verify_right_menu_button.setObjectName("verify_right_menu_button")
        self.verticalLayout_6.addWidget(self.verify_right_menu_button)
        self.guides_right_menu_button_3 = QtGui.QPushButton(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guides_right_menu_button_3.sizePolicy().hasHeightForWidth())
        self.guides_right_menu_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.guides_right_menu_button_3.setFont(font)
        self.guides_right_menu_button_3.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.guides_right_menu_button_3.setFlat(False)
        self.guides_right_menu_button_3.setObjectName("guides_right_menu_button_3")
        self.verticalLayout_6.addWidget(self.guides_right_menu_button_3)
        self.bridges_right_menu_button = QtGui.QPushButton(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bridges_right_menu_button.sizePolicy().hasHeightForWidth())
        self.bridges_right_menu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.bridges_right_menu_button.setFont(font)
        self.bridges_right_menu_button.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.bridges_right_menu_button.setFlat(False)
        self.bridges_right_menu_button.setObjectName("bridges_right_menu_button")
        self.verticalLayout_6.addWidget(self.bridges_right_menu_button)
        self.home_right_menu_button = QtGui.QPushButton(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_right_menu_button.sizePolicy().hasHeightForWidth())
        self.home_right_menu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.home_right_menu_button.setFont(font)
        self.home_right_menu_button.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.home_right_menu_button.setFlat(False)
        self.home_right_menu_button.setObjectName("home_right_menu_button")
        self.verticalLayout_6.addWidget(self.home_right_menu_button)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, 9, 9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.language_switch_2 = QtGui.QComboBox(self.SoftwarePage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_switch_2.sizePolicy().hasHeightForWidth())
        self.language_switch_2.setSizePolicy(sizePolicy)
        self.language_switch_2.setMinimumSize(QtCore.QSize(101, 25))
        self.language_switch_2.setMaximumSize(QtCore.QSize(90, 30))
        self.language_switch_2.setStyleSheet("QComboBox  {\n"
"    border: 1px solid #b58dab;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background-color: #ae83a5;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
" \n"
"QComboBox:editable  {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable  {\n"
"\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on  {\n"
"\n"
"}\n"
" \n"
"QComboBox:on  { /* shift the text when the popup opens */\n"
"\n"
"}\n"
" \n"
"QComboBox::drop-down  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    padding-right: 10px;\n"
"    width: 12px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow  {\n"
"    image: url(:/icons/dropdown.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on  { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"}")
        self.language_switch_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.language_switch_2.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.language_switch_2.setFrame(True)
        self.language_switch_2.setObjectName("language_switch_2")
        self.language_switch_2.addItem("")
        self.language_switch_2.addItem("")
        self.horizontalLayout_7.addWidget(self.language_switch_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.SoftwarePage)
        self.GuidesPage = QtGui.QWidget()
        self.GuidesPage.setObjectName("GuidesPage")
        self.gridLayout_2 = QtGui.QGridLayout(self.GuidesPage)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, 10, -1, 10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.guides_scrollarea = QtGui.QScrollArea(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guides_scrollarea.sizePolicy().hasHeightForWidth())
        self.guides_scrollarea.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 116, 173, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.guides_scrollarea.setPalette(palette)
        self.guides_scrollarea.setAutoFillBackground(True)
        self.guides_scrollarea.setStyleSheet("background-color:rgba(142, 116, 173, 60);")
        self.guides_scrollarea.setFrameShape(QtGui.QFrame.NoFrame)
        self.guides_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.guides_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.guides_scrollarea.setWidgetResizable(True)
        self.guides_scrollarea.setObjectName("guides_scrollarea")
        self.software_scrollarea_widgetcontents_2 = QtGui.QWidget()
        self.software_scrollarea_widgetcontents_2.setGeometry(QtCore.QRect(0, 0, 469, 485))
        self.software_scrollarea_widgetcontents_2.setObjectName("software_scrollarea_widgetcontents_2")
        self.guides_scrollarea.setWidget(self.software_scrollarea_widgetcontents_2)
        self.verticalLayout_8.addWidget(self.guides_scrollarea)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_9.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem11)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem12 = QtGui.QSpacerItem(10, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verify_right_menu_button_2 = QtGui.QPushButton(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verify_right_menu_button_2.sizePolicy().hasHeightForWidth())
        self.verify_right_menu_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.verify_right_menu_button_2.setFont(font)
        self.verify_right_menu_button_2.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.verify_right_menu_button_2.setFlat(False)
        self.verify_right_menu_button_2.setObjectName("verify_right_menu_button_2")
        self.verticalLayout_10.addWidget(self.verify_right_menu_button_2)
        self.software_right_menu_button = QtGui.QPushButton(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.software_right_menu_button.sizePolicy().hasHeightForWidth())
        self.software_right_menu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.software_right_menu_button.setFont(font)
        self.software_right_menu_button.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.software_right_menu_button.setFlat(False)
        self.software_right_menu_button.setObjectName("software_right_menu_button")
        self.verticalLayout_10.addWidget(self.software_right_menu_button)
        self.bridges_right_menu_button_2 = QtGui.QPushButton(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bridges_right_menu_button_2.sizePolicy().hasHeightForWidth())
        self.bridges_right_menu_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.bridges_right_menu_button_2.setFont(font)
        self.bridges_right_menu_button_2.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.bridges_right_menu_button_2.setFlat(False)
        self.bridges_right_menu_button_2.setObjectName("bridges_right_menu_button_2")
        self.verticalLayout_10.addWidget(self.bridges_right_menu_button_2)
        self.home_right_menu_button_2 = QtGui.QPushButton(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_right_menu_button_2.sizePolicy().hasHeightForWidth())
        self.home_right_menu_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.home_right_menu_button_2.setFont(font)
        self.home_right_menu_button_2.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.home_right_menu_button_2.setFlat(False)
        self.home_right_menu_button_2.setObjectName("home_right_menu_button_2")
        self.verticalLayout_10.addWidget(self.home_right_menu_button_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 9, 9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.language_switch_3 = QtGui.QComboBox(self.GuidesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_switch_3.sizePolicy().hasHeightForWidth())
        self.language_switch_3.setSizePolicy(sizePolicy)
        self.language_switch_3.setMinimumSize(QtCore.QSize(101, 25))
        self.language_switch_3.setMaximumSize(QtCore.QSize(90, 30))
        self.language_switch_3.setStyleSheet("QComboBox  {\n"
"    border: 1px solid #b58dab;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background-color: #ae83a5;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
" \n"
"QComboBox:editable  {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable  {\n"
"\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on  {\n"
"\n"
"}\n"
" \n"
"QComboBox:on  { /* shift the text when the popup opens */\n"
"\n"
"}\n"
" \n"
"QComboBox::drop-down  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    padding-right: 10px;\n"
"    width: 12px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow  {\n"
"    image: url(:/icons/dropdown.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on  { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"}")
        self.language_switch_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.language_switch_3.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.language_switch_3.setFrame(True)
        self.language_switch_3.setObjectName("language_switch_3")
        self.language_switch_3.addItem("")
        self.language_switch_3.addItem("")
        self.horizontalLayout_12.addWidget(self.language_switch_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.GuidesPage)
        self.VerifyPage = QtGui.QWidget()
        self.VerifyPage.setObjectName("VerifyPage")
        self.gridLayout_3 = QtGui.QGridLayout(self.VerifyPage)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(10, 10, -1, 10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verify_label_2 = QtGui.QLabel(self.VerifyPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(30)
        font.setWeight(50)
        font.setBold(False)
        self.verify_label_2.setFont(font)
        self.verify_label_2.setStyleSheet("color:white;")
        self.verify_label_2.setObjectName("verify_label_2")
        self.verticalLayout_17.addWidget(self.verify_label_2)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(20, 0, -1, 20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.generate_label = QtGui.QLabel(self.VerifyPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(17)
        font.setWeight(50)
        font.setBold(False)
        self.generate_label.setFont(font)
        self.generate_label.setStyleSheet("color:white;")
        self.generate_label.setObjectName("generate_label")
        self.verticalLayout_11.addWidget(self.generate_label)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame = QtGui.QFrame(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(320, 50))
        self.frame.setMaximumSize(QtCore.QSize(320, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.select_file_button = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_button.sizePolicy().hasHeightForWidth())
        self.select_file_button.setSizePolicy(sizePolicy)
        self.select_file_button.setMinimumSize(QtCore.QSize(106, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.select_file_button.setFont(font)
        self.select_file_button.setStyleSheet("QPushButton {\n"
"background-color: #2a1754;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}")
        self.select_file_button.setObjectName("select_file_button")
        self.horizontalLayout_13.addWidget(self.select_file_button)
        spacerItem16 = QtGui.QSpacerItem(19, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.select_folder_button = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_folder_button.sizePolicy().hasHeightForWidth())
        self.select_folder_button.setSizePolicy(sizePolicy)
        self.select_folder_button.setMinimumSize(QtCore.QSize(106, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.select_folder_button.setFont(font)
        self.select_folder_button.setStyleSheet("QPushButton {\n"
"background-color: #2a1754;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}")
        self.select_folder_button.setObjectName("select_folder_button")
        self.horizontalLayout_13.addWidget(self.select_folder_button)
        spacerItem17 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem17)
        self.horizontalLayout_10.addWidget(self.frame)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_17.addLayout(self.verticalLayout_11)
        self.verify_scroll_area = QtGui.QScrollArea(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verify_scroll_area.sizePolicy().hasHeightForWidth())
        self.verify_scroll_area.setSizePolicy(sizePolicy)
        self.verify_scroll_area.setStyleSheet("background-color:rgba(0, 0, 0, 150);")
        self.verify_scroll_area.setFrameShape(QtGui.QFrame.NoFrame)
        self.verify_scroll_area.setWidgetResizable(True)
        self.verify_scroll_area.setObjectName("verify_scroll_area")
        self.verify_scroll_area_widget_contents = QtGui.QWidget()
        self.verify_scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 152))
        self.verify_scroll_area_widget_contents.setObjectName("verify_scroll_area_widget_contents")
        self.verify_scroll_area.setWidget(self.verify_scroll_area_widget_contents)
        self.verticalLayout_17.addWidget(self.verify_scroll_area)
        spacerItem19 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem19)
        self.gridLayout_3.addLayout(self.verticalLayout_17, 0, 0, 1, 1)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_18.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        spacerItem20 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem21 = QtGui.QSpacerItem(10, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem21)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setSpacing(8)
        self.verticalLayout_19.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.software_right_menu_button_2 = QtGui.QPushButton(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.software_right_menu_button_2.sizePolicy().hasHeightForWidth())
        self.software_right_menu_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.software_right_menu_button_2.setFont(font)
        self.software_right_menu_button_2.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.software_right_menu_button_2.setFlat(False)
        self.software_right_menu_button_2.setObjectName("software_right_menu_button_2")
        self.verticalLayout_19.addWidget(self.software_right_menu_button_2)
        self.guides_right_menu_button = QtGui.QPushButton(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guides_right_menu_button.sizePolicy().hasHeightForWidth())
        self.guides_right_menu_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.guides_right_menu_button.setFont(font)
        self.guides_right_menu_button.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.guides_right_menu_button.setFlat(False)
        self.guides_right_menu_button.setObjectName("guides_right_menu_button")
        self.verticalLayout_19.addWidget(self.guides_right_menu_button)
        self.bridges_right_menu_button_3 = QtGui.QPushButton(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bridges_right_menu_button_3.sizePolicy().hasHeightForWidth())
        self.bridges_right_menu_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.bridges_right_menu_button_3.setFont(font)
        self.bridges_right_menu_button_3.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.bridges_right_menu_button_3.setFlat(False)
        self.bridges_right_menu_button_3.setObjectName("bridges_right_menu_button_3")
        self.verticalLayout_19.addWidget(self.bridges_right_menu_button_3)
        self.home_right_menu_button_3 = QtGui.QPushButton(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_right_menu_button_3.sizePolicy().hasHeightForWidth())
        self.home_right_menu_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.home_right_menu_button_3.setFont(font)
        self.home_right_menu_button_3.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.home_right_menu_button_3.setFlat(False)
        self.home_right_menu_button_3.setObjectName("home_right_menu_button_3")
        self.verticalLayout_19.addWidget(self.home_right_menu_button_3)
        self.horizontalLayout_21.addLayout(self.verticalLayout_19)
        self.verticalLayout_18.addLayout(self.horizontalLayout_21)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem22)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, -1, 9, 9)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem23)
        self.language_switch_5 = QtGui.QComboBox(self.VerifyPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_switch_5.sizePolicy().hasHeightForWidth())
        self.language_switch_5.setSizePolicy(sizePolicy)
        self.language_switch_5.setMinimumSize(QtCore.QSize(101, 25))
        self.language_switch_5.setMaximumSize(QtCore.QSize(90, 30))
        self.language_switch_5.setStyleSheet("QComboBox  {\n"
"    border: 1px solid #b58dab;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background-color: #ae83a5;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
" \n"
"QComboBox:editable  {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable  {\n"
"\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on  {\n"
"\n"
"}\n"
" \n"
"QComboBox:on  { /* shift the text when the popup opens */\n"
"\n"
"}\n"
" \n"
"QComboBox::drop-down  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    padding-right: 10px;\n"
"    width: 12px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow  {\n"
"    image: url(:/icons/dropdown.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on  { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"}")
        self.language_switch_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.language_switch_5.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.language_switch_5.setFrame(True)
        self.language_switch_5.setObjectName("language_switch_5")
        self.language_switch_5.addItem("")
        self.language_switch_5.addItem("")
        self.horizontalLayout_22.addWidget(self.language_switch_5)
        self.verticalLayout_18.addLayout(self.horizontalLayout_22)
        self.gridLayout_3.addLayout(self.verticalLayout_18, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.VerifyPage)
        self.BridgesPage = QtGui.QWidget()
        self.BridgesPage.setObjectName("BridgesPage")
        self.gridLayout_4 = QtGui.QGridLayout(self.BridgesPage)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(10, 10, -1, 10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.get_bridges_label = QtGui.QLabel(self.BridgesPage)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(30)
        font.setWeight(50)
        font.setBold(False)
        self.get_bridges_label.setFont(font)
        self.get_bridges_label.setStyleSheet("color:white;")
        self.get_bridges_label.setObjectName("get_bridges_label")
        self.verticalLayout_12.addWidget(self.get_bridges_label)
        self.bridges_scrollarea = QtGui.QScrollArea(self.BridgesPage)
        self.bridges_scrollarea.setAutoFillBackground(False)
        self.bridges_scrollarea.setStyleSheet("background-color:rgba(142, 116, 173, 60);")
        self.bridges_scrollarea.setFrameShape(QtGui.QFrame.NoFrame)
        self.bridges_scrollarea.setWidgetResizable(True)
        self.bridges_scrollarea.setObjectName("bridges_scrollarea")
        self.bridges_scrollarea_widget_contents = QtGui.QWidget()
        self.bridges_scrollarea_widget_contents.setGeometry(QtCore.QRect(0, 0, 469, 425))
        self.bridges_scrollarea_widget_contents.setObjectName("bridges_scrollarea_widget_contents")
        self.bridges_scrollarea.setWidget(self.bridges_scrollarea_widget_contents)
        self.verticalLayout_12.addWidget(self.bridges_scrollarea)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_20.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        spacerItem24 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem24)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem25 = QtGui.QSpacerItem(10, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem25)
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setSpacing(8)
        self.verticalLayout_21.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.software_right_menu_button_3 = QtGui.QPushButton(self.BridgesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.software_right_menu_button_3.sizePolicy().hasHeightForWidth())
        self.software_right_menu_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.software_right_menu_button_3.setFont(font)
        self.software_right_menu_button_3.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.software_right_menu_button_3.setFlat(False)
        self.software_right_menu_button_3.setObjectName("software_right_menu_button_3")
        self.verticalLayout_21.addWidget(self.software_right_menu_button_3)
        self.guides_right_menu_button_2 = QtGui.QPushButton(self.BridgesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guides_right_menu_button_2.sizePolicy().hasHeightForWidth())
        self.guides_right_menu_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.guides_right_menu_button_2.setFont(font)
        self.guides_right_menu_button_2.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.guides_right_menu_button_2.setFlat(False)
        self.guides_right_menu_button_2.setObjectName("guides_right_menu_button_2")
        self.verticalLayout_21.addWidget(self.guides_right_menu_button_2)
        self.verify_right_menu_button_3 = QtGui.QPushButton(self.BridgesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verify_right_menu_button_3.sizePolicy().hasHeightForWidth())
        self.verify_right_menu_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.verify_right_menu_button_3.setFont(font)
        self.verify_right_menu_button_3.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.verify_right_menu_button_3.setFlat(False)
        self.verify_right_menu_button_3.setObjectName("verify_right_menu_button_3")
        self.verticalLayout_21.addWidget(self.verify_right_menu_button_3)
        self.home_right_menu_button_4 = QtGui.QPushButton(self.BridgesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_right_menu_button_4.sizePolicy().hasHeightForWidth())
        self.home_right_menu_button_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.home_right_menu_button_4.setFont(font)
        self.home_right_menu_button_4.setStyleSheet("background-color: #2a1754;\n"
"color: white;")
        self.home_right_menu_button_4.setFlat(False)
        self.home_right_menu_button_4.setObjectName("home_right_menu_button_4")
        self.verticalLayout_21.addWidget(self.home_right_menu_button_4)
        self.horizontalLayout_23.addLayout(self.verticalLayout_21)
        self.verticalLayout_20.addLayout(self.horizontalLayout_23)
        spacerItem26 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem26)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(-1, -1, 9, 9)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem27)
        self.language_switch_4 = QtGui.QComboBox(self.BridgesPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_switch_4.sizePolicy().hasHeightForWidth())
        self.language_switch_4.setSizePolicy(sizePolicy)
        self.language_switch_4.setMinimumSize(QtCore.QSize(101, 25))
        self.language_switch_4.setMaximumSize(QtCore.QSize(90, 30))
        self.language_switch_4.setStyleSheet("QComboBox  {\n"
"    border: 1px solid #b58dab;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    background-color: #ae83a5;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"}\n"
" \n"
"QComboBox:editable  {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable  {\n"
"\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on  {\n"
"\n"
"}\n"
" \n"
"QComboBox:on  { /* shift the text when the popup opens */\n"
"\n"
"}\n"
" \n"
"QComboBox::drop-down  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    padding-right: 10px;\n"
"    width: 12px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow  {\n"
"    image: url(:/icons/dropdown.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on  { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"}")
        self.language_switch_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.language_switch_4.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.language_switch_4.setFrame(True)
        self.language_switch_4.setObjectName("language_switch_4")
        self.language_switch_4.addItem("")
        self.language_switch_4.addItem("")
        self.horizontalLayout_24.addWidget(self.language_switch_4)
        self.verticalLayout_20.addLayout(self.horizontalLayout_24)
        self.gridLayout_4.addLayout(self.verticalLayout_20, 0, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.stackedWidget.addWidget(self.BridgesPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Satori", None, QtGui.QApplication.UnicodeUTF8))
        self.software_label.setText(QtGui.QApplication.translate("MainForm", "Software", None, QtGui.QApplication.UnicodeUTF8))
        self.bridges_label.setText(QtGui.QApplication.translate("MainForm", "Bridges", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_label.setText(QtGui.QApplication.translate("MainForm", "Verify software", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch.setItemText(0, QtGui.QApplication.translate("MainForm", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch.setItemText(1, QtGui.QApplication.translate("MainForm", "Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_right_menu_button.setText(QtGui.QApplication.translate("MainForm", "Verify Software", None, QtGui.QApplication.UnicodeUTF8))
        self.guides_right_menu_button_3.setText(QtGui.QApplication.translate("MainForm", "How-To Guides", None, QtGui.QApplication.UnicodeUTF8))
        self.bridges_right_menu_button.setText(QtGui.QApplication.translate("MainForm", "Get Tor Bridges", None, QtGui.QApplication.UnicodeUTF8))
        self.home_right_menu_button.setText(QtGui.QApplication.translate("MainForm", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_2.setItemText(0, QtGui.QApplication.translate("MainForm", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_2.setItemText(1, QtGui.QApplication.translate("MainForm", "Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_right_menu_button_2.setText(QtGui.QApplication.translate("MainForm", "Verify Software", None, QtGui.QApplication.UnicodeUTF8))
        self.software_right_menu_button.setText(QtGui.QApplication.translate("MainForm", "Get software", None, QtGui.QApplication.UnicodeUTF8))
        self.bridges_right_menu_button_2.setText(QtGui.QApplication.translate("MainForm", "Get Tor Bridges", None, QtGui.QApplication.UnicodeUTF8))
        self.home_right_menu_button_2.setText(QtGui.QApplication.translate("MainForm", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_3.setItemText(0, QtGui.QApplication.translate("MainForm", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_3.setItemText(1, QtGui.QApplication.translate("MainForm", "Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_label_2.setText(QtGui.QApplication.translate("MainForm", "Verify software", None, QtGui.QApplication.UnicodeUTF8))
        self.generate_label.setText(QtGui.QApplication.translate("MainForm", "Generate sha256 checksum", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file_button.setText(QtGui.QApplication.translate("MainForm", "Select file", None, QtGui.QApplication.UnicodeUTF8))
        self.select_folder_button.setText(QtGui.QApplication.translate("MainForm", "Select folder", None, QtGui.QApplication.UnicodeUTF8))
        self.software_right_menu_button_2.setText(QtGui.QApplication.translate("MainForm", "Get software", None, QtGui.QApplication.UnicodeUTF8))
        self.guides_right_menu_button.setText(QtGui.QApplication.translate("MainForm", "How-To Guides", None, QtGui.QApplication.UnicodeUTF8))
        self.bridges_right_menu_button_3.setText(QtGui.QApplication.translate("MainForm", "Get Tor Bridges", None, QtGui.QApplication.UnicodeUTF8))
        self.home_right_menu_button_3.setText(QtGui.QApplication.translate("MainForm", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_5.setItemText(0, QtGui.QApplication.translate("MainForm", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_5.setItemText(1, QtGui.QApplication.translate("MainForm", "Русский", None, QtGui.QApplication.UnicodeUTF8))
        self.get_bridges_label.setText(QtGui.QApplication.translate("MainForm", "Get Bridges", None, QtGui.QApplication.UnicodeUTF8))
        self.software_right_menu_button_3.setText(QtGui.QApplication.translate("MainForm", "Get software", None, QtGui.QApplication.UnicodeUTF8))
        self.guides_right_menu_button_2.setText(QtGui.QApplication.translate("MainForm", "How-To Guides", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_right_menu_button_3.setText(QtGui.QApplication.translate("MainForm", "Verify software", None, QtGui.QApplication.UnicodeUTF8))
        self.home_right_menu_button_4.setText(QtGui.QApplication.translate("MainForm", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_4.setItemText(0, QtGui.QApplication.translate("MainForm", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.language_switch_4.setItemText(1, QtGui.QApplication.translate("MainForm", "Русский", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
