import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from src.setup_mainwindow import MainScreen

from ui_elements.mainwindow import Ui_MainWindow
from ui_elements.optiondialog import Ui_OptionDialog
from src.msgboxgenerate import standartbox
from ui_elements.paydialog import Ui_PayDialog


def create_main_window(devenvironment, db_path, app_width=480, app_height=320):
    """ Creates the mainwindow, need the path of the DB for it. 
    
    Variables:
        devenvironment (Bool): For development purposes, deactivates imports and commands 
            which are specific to the Raspberry Pi or the use of a touchscreen.
        DB (path): Path to the Database
        app_width (int): Resolution (width) of the touchscreen
        app_height (int): Resolution (height) of the touchscreen
    """
    # creates the application
    app = QApplication(sys.argv)
    #creates the mainscreen, sets it to fixed size and fullscreen
    w = MainScreen(devenvironment, db_path)
    w.showFullScreen()
    w.setFixedSize(app_width, app_height)
    # runs the app until the exit
    sys.exit(app.exec_())
    # at the end closes the DB
    w.DB.close()

