# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'masterdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MasterDialog(object):
    def setupUi(self, MasterDialog):
        MasterDialog.setObjectName("MasterDialog")
        MasterDialog.resize(480, 320)
        MasterDialog.setMinimumSize(QtCore.QSize(480, 320))
        MasterDialog.setMaximumSize(QtCore.QSize(480, 320))
        MasterDialog.setStyleSheet("QWidget\n"
"{\n"
"    color: rgb(0, 123, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    color: rgb(239, 151, 0);\n"
"    border: 1px solid rgb(239, 151, 0);\n"
"    /*color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);    */\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid  rgb(97, 97, 97);\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(97, 97, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    padding: 5px;\n"
"    padding-left: 63px;\n"
"    padding-right:63px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
".QMessageBox {font-size: 16pt}\n"
"\n"
".QSlider {\n"
"    min-height: 30px;\n"
"    max-height: 50px;\n"
"}\n"
"\n"
".QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 5px;\n"
"    background: #393939;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal {\n"
"    background: rgb(0, 123, 255);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin: -24px -12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(97, 97, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(97, 97, 97);\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"    border-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"    border-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background-color: rgb(166, 166, 166);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: rgb(0, 123, 255);\n"
"   /* width: 40px;\n"
"    margin: 0.5px;*/\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: rgb(0, 123, 255);    \n"
"    border: 2px solid  rgb(97, 97, 97);\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    border: 2px solid  rgb(97, 97, 97);\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid rgb(97, 97, 97);\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"\n"
"#CHB_active {\n"
"    color: rgb(239, 151, 0);\n"
"}")
        MasterDialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MasterDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PB_back = QtWidgets.QPushButton(MasterDialog)
        self.PB_back.setMinimumSize(QtCore.QSize(0, 70))
        self.PB_back.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_back.setFont(font)
        self.PB_back.setObjectName("PB_back")
        self.horizontalLayout.addWidget(self.PB_back)
        self.CB_employee = QtWidgets.QComboBox(MasterDialog)
        self.CB_employee.setMinimumSize(QtCore.QSize(105, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CB_employee.setFont(font)
        self.CB_employee.setMaxVisibleItems(6)
        self.CB_employee.setObjectName("CB_employee")
        self.horizontalLayout.addWidget(self.CB_employee)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MasterDialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.LE_first_name = ClickableLineEdit(MasterDialog)
        self.LE_first_name.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LE_first_name.setFont(font)
        self.LE_first_name.setObjectName("LE_first_name")
        self.verticalLayout.addWidget(self.LE_first_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(MasterDialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.LE_last_name = ClickableLineEdit(MasterDialog)
        self.LE_last_name.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LE_last_name.setFont(font)
        self.LE_last_name.setObjectName("LE_last_name")
        self.verticalLayout_2.addWidget(self.LE_last_name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PB_change = QtWidgets.QPushButton(MasterDialog)
        self.PB_change.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_change.setFont(font)
        self.PB_change.setObjectName("PB_change")
        self.horizontalLayout_3.addWidget(self.PB_change)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.CHB_active = QtWidgets.QCheckBox(MasterDialog)
        self.CHB_active.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CHB_active.setFont(font)
        self.CHB_active.setStyleSheet("QCheckBox::indicator \n"
"{\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}")
        self.CHB_active.setObjectName("CHB_active")
        self.horizontalLayout_3.addWidget(self.CHB_active)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(MasterDialog)
        QtCore.QMetaObject.connectSlotsByName(MasterDialog)

    def retranslateUi(self, MasterDialog):
        _translate = QtCore.QCoreApplication.translate
        MasterDialog.setWindowTitle(_translate("MasterDialog", "Dialog"))
        self.PB_back.setText(_translate("MasterDialog", "< Back"))
        self.label.setText(_translate("MasterDialog", "First Name"))
        self.label_2.setText(_translate("MasterDialog", "Last Name"))
        self.PB_change.setText(_translate("MasterDialog", "change"))
        self.CHB_active.setText(_translate("MasterDialog", "  active"))

from ui_elements.clickablelineedit import ClickableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterDialog = QtWidgets.QDialog()
    ui = Ui_MasterDialog()
    ui.setupUi(MasterDialog)
    MasterDialog.show()
    sys.exit(app.exec_())

