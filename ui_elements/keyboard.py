# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Keyboard(object):
    def setupUi(self, Keyboard):
        Keyboard.setObjectName("Keyboard")
        Keyboard.resize(480, 320)
        Keyboard.setMinimumSize(QtCore.QSize(480, 320))
        Keyboard.setMaximumSize(QtCore.QSize(480, 320))
        Keyboard.setStyleSheet("QWidget\n"
"{\n"
"    color: rgb(0, 123, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: (0, 123, 255);\n"
"    border-width: 4px;\n"
"    border-color: rgb(0, 123, 255);\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(239, 151, 0);    \n"
"    border-color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    color: rgb(239, 151, 0);    \n"
"    border-color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    color: (0, 123, 255);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid rgb(97, 97, 97);\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"#LName {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Keyboard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LName = QtWidgets.QLineEdit(Keyboard)
        self.LName.setMinimumSize(QtCore.QSize(0, 50))
        self.LName.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.LName.setFont(font)
        self.LName.setObjectName("LName")
        self.horizontalLayout.addWidget(self.LName)
        self.clear = QtWidgets.QPushButton(Keyboard)
        self.clear.setMinimumSize(QtCore.QSize(80, 0))
        self.clear.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.backButton = QtWidgets.QPushButton(Keyboard)
        self.backButton.setMinimumSize(QtCore.QSize(80, 0))
        self.backButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.Buttonq = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonq.sizePolicy().hasHeightForWidth())
        self.Buttonq.setSizePolicy(sizePolicy)
        self.Buttonq.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonq.setFont(font)
        self.Buttonq.setObjectName("Buttonq")
        self.gridLayout.addWidget(self.Buttonq, 0, 0, 1, 1)
        self.Buttonw = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonw.sizePolicy().hasHeightForWidth())
        self.Buttonw.setSizePolicy(sizePolicy)
        self.Buttonw.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonw.setFont(font)
        self.Buttonw.setObjectName("Buttonw")
        self.gridLayout.addWidget(self.Buttonw, 0, 1, 1, 1)
        self.Buttone = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttone.sizePolicy().hasHeightForWidth())
        self.Buttone.setSizePolicy(sizePolicy)
        self.Buttone.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttone.setFont(font)
        self.Buttone.setObjectName("Buttone")
        self.gridLayout.addWidget(self.Buttone, 0, 2, 1, 1)
        self.Buttont = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttont.sizePolicy().hasHeightForWidth())
        self.Buttont.setSizePolicy(sizePolicy)
        self.Buttont.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttont.setFont(font)
        self.Buttont.setObjectName("Buttont")
        self.gridLayout.addWidget(self.Buttont, 0, 4, 1, 1)
        self.Buttonr = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonr.sizePolicy().hasHeightForWidth())
        self.Buttonr.setSizePolicy(sizePolicy)
        self.Buttonr.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonr.setFont(font)
        self.Buttonr.setObjectName("Buttonr")
        self.gridLayout.addWidget(self.Buttonr, 0, 3, 1, 1)
        self.Buttono = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttono.sizePolicy().hasHeightForWidth())
        self.Buttono.setSizePolicy(sizePolicy)
        self.Buttono.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttono.setFont(font)
        self.Buttono.setObjectName("Buttono")
        self.gridLayout.addWidget(self.Buttono, 0, 8, 1, 1)
        self.Buttonu = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonu.sizePolicy().hasHeightForWidth())
        self.Buttonu.setSizePolicy(sizePolicy)
        self.Buttonu.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonu.setFont(font)
        self.Buttonu.setObjectName("Buttonu")
        self.gridLayout.addWidget(self.Buttonu, 0, 6, 1, 1)
        self.Buttoni = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttoni.sizePolicy().hasHeightForWidth())
        self.Buttoni.setSizePolicy(sizePolicy)
        self.Buttoni.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttoni.setFont(font)
        self.Buttoni.setObjectName("Buttoni")
        self.gridLayout.addWidget(self.Buttoni, 0, 7, 1, 1)
        self.Buttony = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttony.sizePolicy().hasHeightForWidth())
        self.Buttony.setSizePolicy(sizePolicy)
        self.Buttony.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttony.setFont(font)
        self.Buttony.setObjectName("Buttony")
        self.gridLayout.addWidget(self.Buttony, 0, 5, 1, 1)
        self.Buttons = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttons.sizePolicy().hasHeightForWidth())
        self.Buttons.setSizePolicy(sizePolicy)
        self.Buttons.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttons.setFont(font)
        self.Buttons.setObjectName("Buttons")
        self.gridLayout.addWidget(self.Buttons, 2, 1, 1, 1)
        self.Buttond = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttond.sizePolicy().hasHeightForWidth())
        self.Buttond.setSizePolicy(sizePolicy)
        self.Buttond.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttond.setFont(font)
        self.Buttond.setObjectName("Buttond")
        self.gridLayout.addWidget(self.Buttond, 2, 2, 1, 1)
        self.Buttonf = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonf.sizePolicy().hasHeightForWidth())
        self.Buttonf.setSizePolicy(sizePolicy)
        self.Buttonf.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonf.setFont(font)
        self.Buttonf.setObjectName("Buttonf")
        self.gridLayout.addWidget(self.Buttonf, 2, 3, 1, 1)
        self.Buttonl = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonl.sizePolicy().hasHeightForWidth())
        self.Buttonl.setSizePolicy(sizePolicy)
        self.Buttonl.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonl.setFont(font)
        self.Buttonl.setObjectName("Buttonl")
        self.gridLayout.addWidget(self.Buttonl, 2, 8, 1, 1)
        self.Buttonj = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonj.sizePolicy().hasHeightForWidth())
        self.Buttonj.setSizePolicy(sizePolicy)
        self.Buttonj.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonj.setFont(font)
        self.Buttonj.setObjectName("Buttonj")
        self.gridLayout.addWidget(self.Buttonj, 2, 6, 1, 1)
        self.Buttong = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttong.sizePolicy().hasHeightForWidth())
        self.Buttong.setSizePolicy(sizePolicy)
        self.Buttong.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttong.setFont(font)
        self.Buttong.setObjectName("Buttong")
        self.gridLayout.addWidget(self.Buttong, 2, 4, 1, 1)
        self.Buttonh = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonh.sizePolicy().hasHeightForWidth())
        self.Buttonh.setSizePolicy(sizePolicy)
        self.Buttonh.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonh.setFont(font)
        self.Buttonh.setObjectName("Buttonh")
        self.gridLayout.addWidget(self.Buttonh, 2, 5, 1, 1)
        self.Buttonz = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonz.sizePolicy().hasHeightForWidth())
        self.Buttonz.setSizePolicy(sizePolicy)
        self.Buttonz.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonz.setFont(font)
        self.Buttonz.setObjectName("Buttonz")
        self.gridLayout.addWidget(self.Buttonz, 3, 1, 1, 1)
        self.Buttonx = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonx.sizePolicy().hasHeightForWidth())
        self.Buttonx.setSizePolicy(sizePolicy)
        self.Buttonx.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonx.setFont(font)
        self.Buttonx.setObjectName("Buttonx")
        self.gridLayout.addWidget(self.Buttonx, 3, 2, 1, 1)
        self.Buttonv = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonv.sizePolicy().hasHeightForWidth())
        self.Buttonv.setSizePolicy(sizePolicy)
        self.Buttonv.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonv.setFont(font)
        self.Buttonv.setObjectName("Buttonv")
        self.gridLayout.addWidget(self.Buttonv, 3, 4, 1, 1)
        self.Buttonb = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonb.sizePolicy().hasHeightForWidth())
        self.Buttonb.setSizePolicy(sizePolicy)
        self.Buttonb.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonb.setFont(font)
        self.Buttonb.setObjectName("Buttonb")
        self.gridLayout.addWidget(self.Buttonb, 3, 5, 1, 1)
        self.Buttonm = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonm.sizePolicy().hasHeightForWidth())
        self.Buttonm.setSizePolicy(sizePolicy)
        self.Buttonm.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonm.setFont(font)
        self.Buttonm.setObjectName("Buttonm")
        self.gridLayout.addWidget(self.Buttonm, 3, 7, 1, 1)
        self.Buttonn = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonn.sizePolicy().hasHeightForWidth())
        self.Buttonn.setSizePolicy(sizePolicy)
        self.Buttonn.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonn.setFont(font)
        self.Buttonn.setObjectName("Buttonn")
        self.gridLayout.addWidget(self.Buttonn, 3, 6, 1, 1)
        self.enterButton = QtWidgets.QPushButton(Keyboard)
        self.enterButton.setMinimumSize(QtCore.QSize(20, 45))
        self.enterButton.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setObjectName("enterButton")
        self.gridLayout.addWidget(self.enterButton, 4, 1, 1, 7)
        self.Buttonp = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonp.sizePolicy().hasHeightForWidth())
        self.Buttonp.setSizePolicy(sizePolicy)
        self.Buttonp.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonp.setFont(font)
        self.Buttonp.setObjectName("Buttonp")
        self.gridLayout.addWidget(self.Buttonp, 0, 9, 1, 1)
        self.Buttona = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttona.sizePolicy().hasHeightForWidth())
        self.Buttona.setSizePolicy(sizePolicy)
        self.Buttona.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttona.setFont(font)
        self.Buttona.setObjectName("Buttona")
        self.gridLayout.addWidget(self.Buttona, 2, 0, 1, 1)
        self.Buttonc = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonc.sizePolicy().hasHeightForWidth())
        self.Buttonc.setSizePolicy(sizePolicy)
        self.Buttonc.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonc.setFont(font)
        self.Buttonc.setObjectName("Buttonc")
        self.gridLayout.addWidget(self.Buttonc, 3, 3, 1, 1)
        self.shift = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shift.sizePolicy().hasHeightForWidth())
        self.shift.setSizePolicy(sizePolicy)
        self.shift.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.shift.setFont(font)
        self.shift.setStyleSheet("")
        self.shift.setCheckable(True)
        self.shift.setObjectName("shift")
        self.gridLayout.addWidget(self.shift, 3, 0, 2, 1)
        self.Buttonk = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttonk.sizePolicy().hasHeightForWidth())
        self.Buttonk.setSizePolicy(sizePolicy)
        self.Buttonk.setMinimumSize(QtCore.QSize(44, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Buttonk.setFont(font)
        self.Buttonk.setObjectName("Buttonk")
        self.gridLayout.addWidget(self.Buttonk, 2, 7, 1, 1)
        self.dotButton = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy)
        self.dotButton.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")
        self.gridLayout.addWidget(self.dotButton, 2, 9, 1, 1)
        self.delButton = QtWidgets.QPushButton(Keyboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.delButton.setFont(font)
        self.delButton.setCheckable(False)
        self.delButton.setChecked(False)
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 3, 8, 2, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Keyboard)
        QtCore.QMetaObject.connectSlotsByName(Keyboard)

    def retranslateUi(self, Keyboard):
        _translate = QtCore.QCoreApplication.translate
        Keyboard.setWindowTitle(_translate("Keyboard", "Enter Name"))
        self.clear.setText(_translate("Keyboard", "C"))
        self.backButton.setText(_translate("Keyboard", "X"))
        self.Buttonq.setText(_translate("Keyboard", "q"))
        self.Buttonw.setText(_translate("Keyboard", "w"))
        self.Buttone.setText(_translate("Keyboard", "e"))
        self.Buttont.setText(_translate("Keyboard", "t"))
        self.Buttonr.setText(_translate("Keyboard", "r"))
        self.Buttono.setText(_translate("Keyboard", "o"))
        self.Buttonu.setText(_translate("Keyboard", "u"))
        self.Buttoni.setText(_translate("Keyboard", "i"))
        self.Buttony.setText(_translate("Keyboard", "y"))
        self.Buttons.setText(_translate("Keyboard", "s"))
        self.Buttond.setText(_translate("Keyboard", "d"))
        self.Buttonf.setText(_translate("Keyboard", "f"))
        self.Buttonl.setText(_translate("Keyboard", "l"))
        self.Buttonj.setText(_translate("Keyboard", "j"))
        self.Buttong.setText(_translate("Keyboard", "g"))
        self.Buttonh.setText(_translate("Keyboard", "h"))
        self.Buttonz.setText(_translate("Keyboard", "z"))
        self.Buttonx.setText(_translate("Keyboard", "x"))
        self.Buttonv.setText(_translate("Keyboard", "v"))
        self.Buttonb.setText(_translate("Keyboard", "b"))
        self.Buttonm.setText(_translate("Keyboard", "m"))
        self.Buttonn.setText(_translate("Keyboard", "n"))
        self.enterButton.setText(_translate("Keyboard", "Enter"))
        self.Buttonp.setText(_translate("Keyboard", "p"))
        self.Buttona.setText(_translate("Keyboard", "a"))
        self.Buttonc.setText(_translate("Keyboard", "c"))
        self.shift.setText(_translate("Keyboard", "^"))
        self.Buttonk.setText(_translate("Keyboard", "k"))
        self.dotButton.setText(_translate("Keyboard", "."))
        self.delButton.setText(_translate("Keyboard", "del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Keyboard = QtWidgets.QDialog()
    ui = Ui_Keyboard()
    ui.setupUi(Keyboard)
    Keyboard.show()
    sys.exit(app.exec_())

