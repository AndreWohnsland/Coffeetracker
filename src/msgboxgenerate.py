import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *


def standartbox(textstring, boxtype="standard", okstring="OK", cancelstring="Cancel", parent=None, devenvironment=True):
    """ The default messagebox for the Maker. Uses a QMessageBox with OK-Button 
    Boxtypes are:
        standard: Only an ok button and a text
        okcancel: Text with option to okay or cancel 
    """
    # print(textstring)
    msgBox = QMessageBox(parent)
    if boxtype == "standard":
        msgBox.setStandardButtons(QMessageBox.Ok)   
    elif boxtype == "okcancel":
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        buttoncancel = msgBox.button(QMessageBox.Cancel)
        buttoncancel.setText("{: ^12}".format(cancelstring))
    buttonok = msgBox.button(QMessageBox.Ok)
    buttonok.setText("{: ^12}".format(okstring))
    fillstring = "-" * 40
    msgBox.setText("{0}\n{1}\n{0}".format(fillstring, textstring))
    if not devenvironment:
        msgBox.setCursor(Qt.BlankCursor)
    msgBox.showFullScreen()
    msgBox.setStyleSheet(
        "QMessageBox QPushButton{background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); color: rgb(0, 0, 0); font-size: 30pt;} QMessageBox{background-color: rgb(10, 10, 10); font-size: 16pt;} QMessageBox QLabel{background-color: rgb(10, 10, 10); color: rgb(0, 123, 255); font-size: 16pt;}")
    retval = msgBox.exec_()
    if boxtype == "okcancel":
        # print("value of pressed message box button:", retval)
        return retval
