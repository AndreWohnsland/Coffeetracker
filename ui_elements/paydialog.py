# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paydialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PayDialog(object):
    def setupUi(self, PayDialog):
        PayDialog.setObjectName("PayDialog")
        PayDialog.resize(480, 320)
        PayDialog.setMinimumSize(QtCore.QSize(480, 320))
        PayDialog.setMaximumSize(QtCore.QSize(480, 320))
        PayDialog.setStyleSheet("QWidget\n"
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
"#LE_last_name {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"#LE_first_name {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"#L_user {\n"
"    color: rgb(239, 151, 0);\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PayDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PB_back = QtWidgets.QPushButton(PayDialog)
        self.PB_back.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_back.setFont(font)
        self.PB_back.setObjectName("PB_back")
        self.horizontalLayout.addWidget(self.PB_back)
        self.PB_pay = QtWidgets.QPushButton(PayDialog)
        self.PB_pay.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_pay.setFont(font)
        self.PB_pay.setObjectName("PB_pay")
        self.horizontalLayout.addWidget(self.PB_pay)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(PayDialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.LE_credit = ClickableLineEdit(PayDialog)
        self.LE_credit.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LE_credit.setFont(font)
        self.LE_credit.setObjectName("LE_credit")
        self.verticalLayout_3.addWidget(self.LE_credit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.L_user = QtWidgets.QLabel(PayDialog)
        self.L_user.setMinimumSize(QtCore.QSize(300, 0))
        self.L_user.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.L_user.setFont(font)
        self.L_user.setAlignment(QtCore.Qt.AlignCenter)
        self.L_user.setObjectName("L_user")
        self.horizontalLayout_3.addWidget(self.L_user)
        self.PB_undo = QtWidgets.QPushButton(PayDialog)
        self.PB_undo.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_undo.setFont(font)
        self.PB_undo.setObjectName("PB_undo")
        self.horizontalLayout_3.addWidget(self.PB_undo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PayDialog)
        QtCore.QMetaObject.connectSlotsByName(PayDialog)

    def retranslateUi(self, PayDialog):
        _translate = QtCore.QCoreApplication.translate
        PayDialog.setWindowTitle(_translate("PayDialog", "Dialog"))
        self.PB_back.setText(_translate("PayDialog", "< Back"))
        self.PB_pay.setText(_translate("PayDialog", "Pay"))
        self.label.setText(_translate("PayDialog", "Credit to add to:"))
        self.L_user.setText(_translate("PayDialog", "Username"))
        self.PB_undo.setText(_translate("PayDialog", "Undo Last"))

from clickablelineedit import ClickableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PayDialog = QtWidgets.QDialog()
    ui = Ui_PayDialog()
    ui.setupUi(PayDialog)
    PayDialog.show()
    sys.exit(app.exec_())

