# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numpad.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_numpadwindow(object):
    def setupUi(self, numpadwindow):
        numpadwindow.setObjectName("numpadwindow")
        numpadwindow.resize(480, 320)
        numpadwindow.setMinimumSize(QtCore.QSize(480, 320))
        numpadwindow.setMaximumSize(QtCore.QSize(480, 320))
        numpadwindow.setStyleSheet("QWidget\n"
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
"QLineEdit\n"
"{\n"
"    color: (0, 123, 255);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid rgb(97, 97, 97);\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"#LE_money {\n"
"    color: rgb(239, 151, 0);\n"
"}")
        numpadwindow.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(numpadwindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PB_cancel = QtWidgets.QPushButton(numpadwindow)
        self.PB_cancel.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB_cancel.setFont(font)
        self.PB_cancel.setObjectName("PB_cancel")
        self.verticalLayout.addWidget(self.PB_cancel)
        self.LE_money = QtWidgets.QLineEdit(numpadwindow)
        self.LE_money.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.LE_money.setFont(font)
        self.LE_money.setObjectName("LE_money")
        self.verticalLayout.addWidget(self.LE_money)
        self.PB_ok = QtWidgets.QPushButton(numpadwindow)
        self.PB_ok.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.PB_ok.setFont(font)
        self.PB_ok.setObjectName("PB_ok")
        self.verticalLayout.addWidget(self.PB_ok)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PB4 = QtWidgets.QPushButton(numpadwindow)
        self.PB4.setMinimumSize(QtCore.QSize(95, 50))
        self.PB4.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB4.setFont(font)
        self.PB4.setObjectName("PB4")
        self.gridLayout.addWidget(self.PB4, 1, 0, 1, 1)
        self.PB1 = QtWidgets.QPushButton(numpadwindow)
        self.PB1.setMinimumSize(QtCore.QSize(95, 50))
        self.PB1.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB1.setFont(font)
        self.PB1.setObjectName("PB1")
        self.gridLayout.addWidget(self.PB1, 0, 0, 1, 1)
        self.PB7 = QtWidgets.QPushButton(numpadwindow)
        self.PB7.setMinimumSize(QtCore.QSize(95, 50))
        self.PB7.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB7.setFont(font)
        self.PB7.setObjectName("PB7")
        self.gridLayout.addWidget(self.PB7, 2, 0, 1, 1)
        self.PBdot = QtWidgets.QPushButton(numpadwindow)
        self.PBdot.setMinimumSize(QtCore.QSize(95, 50))
        self.PBdot.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PBdot.setFont(font)
        self.PBdot.setObjectName("PBdot")
        self.gridLayout.addWidget(self.PBdot, 3, 0, 1, 1)
        self.PB8 = QtWidgets.QPushButton(numpadwindow)
        self.PB8.setMinimumSize(QtCore.QSize(95, 50))
        self.PB8.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB8.setFont(font)
        self.PB8.setObjectName("PB8")
        self.gridLayout.addWidget(self.PB8, 2, 1, 1, 1)
        self.PB2 = QtWidgets.QPushButton(numpadwindow)
        self.PB2.setMinimumSize(QtCore.QSize(95, 50))
        self.PB2.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB2.setFont(font)
        self.PB2.setObjectName("PB2")
        self.gridLayout.addWidget(self.PB2, 0, 1, 1, 1)
        self.PB5 = QtWidgets.QPushButton(numpadwindow)
        self.PB5.setMinimumSize(QtCore.QSize(95, 50))
        self.PB5.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB5.setFont(font)
        self.PB5.setObjectName("PB5")
        self.gridLayout.addWidget(self.PB5, 1, 1, 1, 1)
        self.PB0 = QtWidgets.QPushButton(numpadwindow)
        self.PB0.setMinimumSize(QtCore.QSize(95, 50))
        self.PB0.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB0.setFont(font)
        self.PB0.setObjectName("PB0")
        self.gridLayout.addWidget(self.PB0, 3, 1, 1, 1)
        self.PB3 = QtWidgets.QPushButton(numpadwindow)
        self.PB3.setMinimumSize(QtCore.QSize(95, 50))
        self.PB3.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB3.setFont(font)
        self.PB3.setObjectName("PB3")
        self.gridLayout.addWidget(self.PB3, 0, 2, 1, 1)
        self.PB6 = QtWidgets.QPushButton(numpadwindow)
        self.PB6.setMinimumSize(QtCore.QSize(95, 50))
        self.PB6.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB6.setFont(font)
        self.PB6.setObjectName("PB6")
        self.gridLayout.addWidget(self.PB6, 1, 2, 1, 1)
        self.PB9 = QtWidgets.QPushButton(numpadwindow)
        self.PB9.setMinimumSize(QtCore.QSize(95, 50))
        self.PB9.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PB9.setFont(font)
        self.PB9.setObjectName("PB9")
        self.gridLayout.addWidget(self.PB9, 2, 2, 1, 1)
        self.PBdel = QtWidgets.QPushButton(numpadwindow)
        self.PBdel.setMinimumSize(QtCore.QSize(95, 50))
        self.PBdel.setMaximumSize(QtCore.QSize(110, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.PBdel.setFont(font)
        self.PBdel.setObjectName("PBdel")
        self.gridLayout.addWidget(self.PBdel, 3, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(numpadwindow)
        QtCore.QMetaObject.connectSlotsByName(numpadwindow)

    def retranslateUi(self, numpadwindow):
        _translate = QtCore.QCoreApplication.translate
        numpadwindow.setWindowTitle(_translate("numpadwindow", "Pay amount"))
        self.PB_cancel.setText(_translate("numpadwindow", "Cancel"))
        self.PB_ok.setText(_translate("numpadwindow", "OK"))
        self.PB4.setText(_translate("numpadwindow", "4"))
        self.PB1.setText(_translate("numpadwindow", "1"))
        self.PB7.setText(_translate("numpadwindow", "7"))
        self.PBdot.setText(_translate("numpadwindow", "."))
        self.PB8.setText(_translate("numpadwindow", "8"))
        self.PB2.setText(_translate("numpadwindow", "2"))
        self.PB5.setText(_translate("numpadwindow", "5"))
        self.PB0.setText(_translate("numpadwindow", "0"))
        self.PB3.setText(_translate("numpadwindow", "3"))
        self.PB6.setText(_translate("numpadwindow", "6"))
        self.PB9.setText(_translate("numpadwindow", "9"))
        self.PBdel.setText(_translate("numpadwindow", "del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    numpadwindow = QtWidgets.QDialog()
    ui = Ui_numpadwindow()
    ui.setupUi(numpadwindow)
    numpadwindow.show()
    sys.exit(app.exec_())

