import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.paydialog import Ui_PayDialog
from src.msgboxgenerate import standartbox

class PayDialog(QDialog, Ui_PayDialog):
    """ Opens up a dialog where the user can pay his debts. """

    def __init__(self, parent):
        """ Init function for the OptionDialog class. """
        super(PayDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.employee_name = self.ms.employee_name
        self.employee_id = self.ms.employee_id
        self.L_user.setText(self.employee_name)
        # connects all the function
        self.PB_back.clicked.connect(self.back_clicked)
        self.PB_pay.clicked.connect(self.pay_clicked)
        self.PB_undo.clicked.connect(self.undo_clicked)
        self.LE_credit.clicked.connect(lambda: self.ms.lineedit_clicked(self.LE_credit, inputtype="np"))
        # sets limitation
        self.LE_credit.textChanged.connect(lambda: self.ms.lineedit_changed_number(self.LE_credit))

    def pay_clicked(self):
        """ First asks the user to proceed then enters the value into db. """
        enter_credit = False
        pay_amount = self.LE_credit.text()
        # Only carries on if a value is given
        if pay_amount == "":
            standartbox("No value to pay given!")
        else:
            # rounds the number down to two digits (best is to limit it even that way)
            pay_amount = round(float(pay_amount),2)
            user_return = standartbox("Pay amount entered is: {} €".format(pay_amount), boxtype="okcancel", okstring="Enter")
            # if the user return is ok (value 1024 in qt) then set the variable to carry on
            if user_return == 1024:
                enter_credit = True
        # finally enters the data into the db and deletes the entry LE/ updates the label
        if enter_credit:
            self.ms.c.execute("UPDATE OR IGNORE employees SET money = money + ? WHERE ID = ?",(pay_amount, self.employee_id))
            new_money = self.ms.c.execute("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
            self.ms.DB.commit()
            self.LE_credit.setText("")
            standartbox("Your payment has been entered!")
            self.ms.update_money_shown(new_money)
    
    def undo_clicked(self):
        """ Undo the last quantity entry. It just removes one time payment and amount from the list """
        # asks the user if he wants to remove his last entry, if so, carries on in the process
        user_return = standartbox("Remove the last entry for this employee?", boxtype="okcancel", okstring="Yes", cancelstring="No")
        if user_return == 1024:
            current_money = self.ms.c.execute("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
            new_money = current_money + self.ms.quantcosts
            self.ms.c.execute("UPDATE OR IGNORE employees SET money = ?, amount = amount - 1 WHERE ID = ?",(new_money, self.employee_id))
            # deletes the last entry of the employee in the tracking list
            self.ms.c.execute("DELETE FROM tracks WHERE Number=(SELECT max(Number) FROM tracks WHERE employee_ID=?)",(self.employee_id,))
            self.ms.DB.commit()
            # sets the label according to the credit
            self.ms.update_money_shown(new_money)

    def back_clicked(self):
        """ Closes the window without any further action. """
        self.close()
