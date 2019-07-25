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
from src.setup_masterdialog import MasterDialog
from src.setup_plotdialog import PlotDialog

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
        self.PB_add_employee.clicked.connect(lambda: self.ms.add_employee_clicked(self.LE_first_name, self.LE_last_name))
        self.PB_master.clicked.connect(self.master_clicked)
        self.LE_first_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_first_name))
        self.LE_last_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_last_name))

    def back_clicked(self):
        """ Close the window without any further action. """
        self.close()

    def leaderboard_clicked(self):
        """ Plots a graph of the all time leaderboard (or maybe select between active and non active). """
        self.ms.plotdialog = PlotDialog(self.ms)
        self.ms.plotdialog.showFullScreen()

    def master_clicked(self):
        """ Opens up the master dialog. """
        self.ms.masterdialog = MasterDialog(self.ms)
        self.ms.masterdialog.showFullScreen()