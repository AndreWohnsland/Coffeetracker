import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.masterdialog import Ui_MasterDialog
from src.msgboxgenerate import standartbox

class MasterDialog(QDialog, Ui_MasterDialog):
    """ Opens up the masterdialog when the button on the optionscreen is clicked
    Inherits the properties from the mainwindow.
    """

    def __init__(self, parent):
        """ Init function for the MasterDialog class. """
        super(MasterDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.fill_combobox()
        self.employee_id = 0
        # connect the buttons
        self.PB_change.clicked.connect(self.change_clicked)
        self.PB_back.clicked.connect(self.back_clicked)
        self.CB_employee.activated.connect(self.combobox_change)
        self.LE_first_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_first_name))
        self.LE_last_name.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_last_name))

    def change_clicked(self):
        """ Change the employee entried (name and active/inactive). """
        # only runs if the CB is not empy
        if self.CB_employee.currentText() == "":
            standartbox("No employee selected!", parent=self)
        else:
            # the method of the ms can interrupt it the entry is not correct, therefore it returns only true if it ran without only error
            runfill = self.ms.add_employee_clicked(self.LE_first_name, self.LE_last_name, update=True, id=self.employee_id, checkbox_object=self.CHB_active)
            if runfill:
                self.CB_employee.clear()
                self.LE_first_name.clear()
                self.LE_last_name.clear()
                self.fill_combobox()

    def combobox_change(self):
        """ Gets the first and last name, as well the status from the employee. """
        full_name = self.CB_employee.currentText()
        # if the selected item is not empty, gets the name and assigns the id to the class. Also sets the checkbox to DB value
        if full_name != "":
            first_name, last_name = full_name.split()
            self.employee_id, enabled = self.ms.c.execute("SELECT ID, enabled FROM employees WHERE first_name = ? and last_name = ?",(first_name, last_name)).fetchone()[0:2]
            self.LE_first_name.setText(first_name)
            self.LE_last_name.setText(last_name)
            if enabled:
                self.CHB_active.setChecked(True)
            else:
                self.CHB_active.setChecked(False)
        # if none is selected erase all fields
        else:
            self.LE_first_name.setText("")
            self.LE_last_name.setText("")
            self.CHB_active.setChecked(False)
            self.employee_id = 0

    def fill_combobox(self):
        """ Gets all the values op employees into the cb. """
        sqlstring = "SELECT first_name, last_name from employees ORDER BY last_name ASC"
        self.CB_employee.addItem("")
        for employee in self.ms.c.execute(sqlstring):
            self.CB_employee.addItem(" ".join((employee[0], employee[1])))

    def back_clicked(self):
        """ Closes the window without any further action. """
        self.close()
