# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotDialog(object):
    def setupUi(self, PlotDialog):
        PlotDialog.setObjectName("PlotDialog")
        PlotDialog.resize(480, 320)
        PlotDialog.setMinimumSize(QtCore.QSize(480, 320))
        PlotDialog.setMaximumSize(QtCore.QSize(480, 320))
        PlotDialog.setStyleSheet("QWidget\n"
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
"/*\n"
"#L_text {\n"
"    color: rgb(239, 151, 0);\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PlotDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PB_back = QtWidgets.QPushButton(PlotDialog)
        self.PB_back.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_back.setFont(font)
        self.PB_back.setObjectName("PB_back")
        self.horizontalLayout.addWidget(self.PB_back)
        self.PB_dummy = QtWidgets.QPushButton(PlotDialog)
        self.PB_dummy.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_dummy.setFont(font)
        self.PB_dummy.setObjectName("PB_dummy")
        self.horizontalLayout.addWidget(self.PB_dummy)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.L_text = QtWidgets.QLabel(PlotDialog)
        self.L_text.setMinimumSize(QtCore.QSize(0, 110))
        self.L_text.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.L_text.setFont(font)
        self.L_text.setAlignment(QtCore.Qt.AlignCenter)
        self.L_text.setObjectName("L_text")
        self.verticalLayout_3.addWidget(self.L_text)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PB_plot_active = QtWidgets.QPushButton(PlotDialog)
        self.PB_plot_active.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_plot_active.setFont(font)
        self.PB_plot_active.setObjectName("PB_plot_active")
        self.horizontalLayout_3.addWidget(self.PB_plot_active)
        self.PB_plot_all = QtWidgets.QPushButton(PlotDialog)
        self.PB_plot_all.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PB_plot_all.setFont(font)
        self.PB_plot_all.setObjectName("PB_plot_all")
        self.horizontalLayout_3.addWidget(self.PB_plot_all)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PlotDialog)
        QtCore.QMetaObject.connectSlotsByName(PlotDialog)

    def retranslateUi(self, PlotDialog):
        _translate = QtCore.QCoreApplication.translate
        PlotDialog.setWindowTitle(_translate("PlotDialog", "Dialog"))
        self.PB_back.setText(_translate("PlotDialog", "< Back"))
        self.PB_dummy.setText(_translate("PlotDialog", "dummy"))
        self.L_text.setText(_translate("PlotDialog", "<html><head/><body><p><span style=\" font-size:20pt;\">You can choose between lifetime </span></p><p><span style=\" font-size:20pt;\">or only active employees</span></p></body></html>"))
        self.PB_plot_active.setText(_translate("PlotDialog", "plot active"))
        self.PB_plot_all.setText(_translate("PlotDialog", "plot all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotDialog = QtWidgets.QDialog()
    ui = Ui_PlotDialog()
    ui.setupUi(PlotDialog)
    PlotDialog.show()
    sys.exit(app.exec_())

