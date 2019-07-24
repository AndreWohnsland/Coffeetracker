import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.optiondialog import Ui_OptionDialog
from src.msgboxgenerate import standartbox

class OptionDialog(QDialog, Ui_OptionDialog):
    """ Opens up the optiondialog when the button on the mainscreen is clicked
    Inherits the properties from the mainwindow.
    """

    def __init__(self, parent):
        """ Init function for the OptionDialog class. """
        super(OptionDialog, self).__init__(parent)
        self.setupUi(self)
        self.ms = parent
        # connects the buttons
        self.PB_back.clicked.connect(self.back_clicked)
        self.PB_leaderboard.clicked.connect(self.leaderboard_clicked)
        self.PB_add_employee.clicked.connect(self.add_employee_clicked)
        self.LE_first_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_first_name))
        self.LE_last_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_last_name))

    def back_clicked(self):
        """ Close the window without any further action. """
        self.close()

    def add_employee_clicked(self):
        """ Adds the employee to the DB if not already exisiting and all Names are given and at least 3 chars. """
        # replace all the spaces (we want only one first and one last name!)
        first_name = self.LE_first_name.text().replace(" ","").capitalize() 
        last_name  = self.LE_last_name.text().replace(" ","").capitalize() 
        # checks if any is empty or less than thress
        if first_name == "" or last_name == "":
            standartbox("At least one of the names is missing!")
        elif len(first_name)<3 or len(last_name)<3:
            standartbox("The names need at least three character!")
        else:
            # checks if already exists, else enter into the DB
            name_exists = self.ms.c.execute("SELECT COUNT(*) FROM employees WHERE first_name = ? AND last_name = ?",(first_name, last_name)).fetchone()[0]
            if not name_exists:
                self.ms.c.execute("INSERT OR IGNORE INTO employees(first_name, last_name, amount, money, enabled) VALUES(?,?,0,0,1)",(first_name, last_name))
                self.ms.DB.commit()
                self.LE_first_name.clear()
                self.LE_last_name.clear()
                standartbox("Employee {} {} was generated!".format(first_name, last_name))
                self.ms.CB_employee.addItem(" ".join((first_name, last_name)))
                self.ms.CB_employee.model().sort(0)
            else:
                standartbox("This employee already exists!")

    def leaderboard_clicked(self):
        """ Plots a graph of the all time leaderboard (or maybe select between active and non active). """
        pass