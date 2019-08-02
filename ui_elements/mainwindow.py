# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet("QWidget\n"
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
"#L_money {\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"#L_paymentcall{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CB_employee = QtWidgets.QComboBox(self.centralwidget)
        self.CB_employee.setMinimumSize(QtCore.QSize(105, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CB_employee.setFont(font)
        self.CB_employee.setMaxVisibleItems(5)
        self.CB_employee.setObjectName("CB_employee")
        self.horizontalLayout.addWidget(self.CB_employee)
        self.L_money = QtWidgets.QLabel(self.centralwidget)
        self.L_money.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.L_money.setFont(font)
        self.L_money.setAlignment(QtCore.Qt.AlignCenter)
        self.L_money.setObjectName("L_money")
        self.horizontalLayout.addWidget(self.L_money)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.L_paymentcall = QtWidgets.QLabel(self.centralwidget)
        self.L_paymentcall.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.L_paymentcall.setFont(font)
        self.L_paymentcall.setAlignment(QtCore.Qt.AlignCenter)
        self.L_paymentcall.setObjectName("L_paymentcall")
        self.verticalLayout.addWidget(self.L_paymentcall)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.PB_add_quant = QtWidgets.QPushButton(self.centralwidget)
        self.PB_add_quant.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_add_quant.setFont(font)
        self.PB_add_quant.setObjectName("PB_add_quant")
        self.verticalLayout.addWidget(self.PB_add_quant)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PB_pay = QtWidgets.QPushButton(self.centralwidget)
        self.PB_pay.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_pay.setFont(font)
        self.PB_pay.setObjectName("PB_pay")
        self.horizontalLayout_2.addWidget(self.PB_pay)
        self.PB_options = QtWidgets.QPushButton(self.centralwidget)
        self.PB_options.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_options.setFont(font)
        self.PB_options.setObjectName("PB_options")
        self.horizontalLayout_2.addWidget(self.PB_options)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cofeetracker"))
        self.label.setText(_translate("MainWindow", "Select name / choose option"))
        self.L_money.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ef9700;\">Credit</span></p></body></html>"))
        self.L_paymentcall.setText(_translate("MainWindow", "please consider paying debts"))
        self.PB_add_quant.setText(_translate("MainWindow", "Add one coffe to employee"))
        self.PB_pay.setText(_translate("MainWindow", "Pay my debts"))
        self.PB_options.setText(_translate("MainWindow", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

