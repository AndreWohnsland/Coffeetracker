import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.mainwindow import Ui_MainWindow
from ui_elements.optiondialog import Ui_OptionDialog
from src.msgboxgenerate import standartbox


class MainScreen(QMainWindow, Ui_MainWindow):
    """ Creates the mainwindow where the user will be on startup.

        Attributes for Init:
            devenvironment (Bool): For development purposes, deactivates imports and commands 
                which are specific to the Raspberry Pi or the use of a touchscreen.
            DB (path): Path to the Database, or where the DB will be stored.
    """

    def __init__(self, devenvironment, db_path=None, parent=None):
        """ Init function for the MainWindow Class. """
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        # as long as its not devenvironment (usually touchscreen) hide the cursor
        self.devenvironment = devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        # connect to the DB, if one is given (you should always give one!)
        if db_path is not None:
            self.DB = sqlite3.connect(db_path)
            self.c = self.DB.cursor()
        # connects the buttons with the according functions
        self.PB_add_quant.clicked.connect(self.add_quant_clicked)
        self.PB_options.clicked.connect(self.options_clicked)
        self.PB_pay.clicked.connect(self.pay_clicked)
        self.CB_employee.activated.connect(lambda: self.combobox_change(self.CB_employee))
        # loads all the active names into the DB
        sqlstring = "SELECT first_name, last_name from employees WHERE enabled = 1"
        self.CB_employee.addItem("")
        for employee in self.c.execute(sqlstring):
            self.CB_employee.addItem(" ".join((employee[0], employee[1])))

    def add_quant_clicked(self):
        """ Adds one quantity to the employee. """
        employee_name = self.CB_employee.currentText()
        # if there is an employee selected, gets the first and the last name and search into the db, insert the values
        if employee_name != "":
            # split the cb (since it displays first and lastname as onne)
            first_name, last_name = employee_name.split()
            exist_employee, employee_id = self.c.execute("SELECT COUNT(*), ID FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0:2]
            if exist_employee:
                # also gets the time to insert into the tracking table, the costs are currently here as dummy, later a better solution needs to established
                dummy_costs = 0.25
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.c.execute("UPDATE OR IGNORE employees SET amount = amount + 1, money = money + ? WHERE first_name = ? and last_name = ?", (dummy_costs, first_name, last_name))
                self.c.execute("INSERT OR IGNORE INTO tracks(employee_ID, time) VALUES(?, ?)", (employee_id, time_now))
                self.DB.commit()
            else:
                # this should never happen
                standartbox("Ough! Somehow the employee don't exist in the Database!")
        else:
            # if the user didnt select a name it will fail.
            standartbox("Please select a name!")

    
    def pay_clicked(self):
        """ Gives the user the ability to pay his debts. """
        pass
    
    def options_clicked(self):
        """ Opens up the option dialog to chose different options and enter new users. """
        self.optionwindow = OptionDialog(self)
        self.optionwindow.showFullScreen()

    def combobox_change(self, cb_object):
        """ Code gets called each time when the combobox is changed by a user, to refresh the money/debts. """
        pass


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
        self.LE_first_name.clicked.connect(lambda: self.lineedit_clicked(self.LE_first_name))
        self.LE_last_name.clicked.connect(lambda: self.lineedit_clicked(self.LE_last_name))

    def back_clicked(self):
        """ Close the window without any further action. """
        self.close()

    def add_employee_clicked(self):
        """ Adds the employee to the DB if not already exisiting and all Names are given and at least 3 chars. """
        # replace all the spaces (we want only one first and one last name!)
        first_name = self.LE_first_name.text().replace(" ","")
        last_name  = self.LE_last_name.text().replace(" ","")
        # checks if any is empty or less than thress
        if first_name == "" or last_name == "":
            standartbox("At least one of the Names is missing!")
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
                standartbox("Employee was generated!")
            else:
                standartbox("This employee already exists!")

    def leaderboard_clicked(self):
        """ Plots a graph of the all time leaderboard (or maybe select between active and non active). """
        pass

    def lineedit_clicked(self, le_to_write):
        """ Calls a keyboard to write text into a line edit. """
        pass


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

