import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.plotdialog import Ui_PlotDialog
from src.msgboxgenerate import standartbox

class PlotDialog(QDialog, Ui_PlotDialog):
    """ Opens up the plotdialog when the button on the optionscreen is clicked
    Inherits the properties from the mainwindow.
    """

    def __init__(self, parent):
        """ Init function for the MasterDialog class. """
        super(PlotDialog, self).__init__(parent)
        self.setupUi(self)
        self.ms = parent
        # connect the buttons
        self.PB_plot_active.clicked.connect(lambda: self.plot_clicked(active=True))
        self.PB_plot_all.clicked.connect(lambda: self.plot_clicked(active=False))
        self.PB_back.clicked.connect(self.back_clicked)

    def back_clicked(self):
        """ Closes the window without any further action. """
        self.close()

    def plot_clicked(self, active=True):
        """ Plot a leaderboard of the best x employees. By best is ment the most entries. 
        Differentiates between all DB entries, and only still active employees.
        """
        # Selects the 5 employes with the highest comsumption either from all ore active
        if active:
            bonusstring = " WHERE enabled=1"
        else:
            bonusstring = ""
        employee_data = self.ms.c.execute("SELECT first_name, last_name, amount FROM employees{} ORDER BY amount DESC".format(bonusstring))
        namelist = []
        amountlist =  []
        # generates a list of the employees and values for later plotting, currently only prints them out
        for number, row in enumerate(employee_data):
            if number == 5:
                break
            last_name = row[1]
            namelist.append("{} {}.".format(row[0], last_name[0]))
            amountlist.append(row[2])
        print(20*"-")
        for name, amount in zip(namelist, amountlist):
            print(name, amount)

