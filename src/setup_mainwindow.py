import sys
import sqlite3
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.mainwindow import Ui_MainWindow
from src.msgboxgenerate import standartbox
from src.setup_optiondialog import OptionDialog
from src.setup_paydialog import PayDialog
from src.setup_numpad import NumpadScreen
from src.setup_keyboard import KeyboardWidget
from src.loggerconfig import logerror

class MainScreen(QMainWindow, Ui_MainWindow):
    """ Creates the mainwindow where the user will be on startup.

    Attributes for Init:
        -- devenvironment (Bool): For development purposes, deactivates imports and commands 
            which are specific to the Raspberry Pi or the use of a touchscreen.
        -- DB (path): Path to the Database, or where the DB will be stored.
        -- paymentcall_threshold (int or float): Value at which debts the call to payment label is shown.
        -- quantcost (float): Cost of one quantity in Euro.
        -- quantname (string): Name for the quantity
    """

    def __init__(self, devenvironment, db_path=None, paymentcall_threshold=20, quantcosts=0.25, quantname="coffee", parent=None):
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
        self.CB_employee.activated.connect(self.combobox_change)
        # loads all the active names into the DB
        self.fillenabled_combobox()
        self.L_money.setText("")
        self.L_paymentcall.setText("")
        # Generates the ID, the Name and the first/last name
        self.employee_name = ""
        self.employee_first_name = ""
        self.employee_last_name = ""
        self.employee_id = 0
        # assigns the two values for calculating the threshold and the cost of one quantity
        self.quantcosts = quantcosts
        self.paymentcall_threshold = paymentcall_threshold
        # sets a critical threshold where the User gets some more pressure to pay his debts
        # this could be in form of an email or an addition window promt form
        # this is a factor of the normal payment call, it can depent on the product
        # currently it is 1.5 of the normal threshold
        self.critical_threshold = self.paymentcall_threshold * 1.5
        # if there shall be another quantity name than coffee, so be it
        self.quantname = quantname
        self.PB_add_quant.setText(f"Add {self.quantname} to user")

    def add_quant_clicked(self):
        """ Adds one quantity to the employee. """
        # if there is an employee selected, gets the first and the last name and search into the db, insert the values
        enter_quant = False
        if self.employee_name == "":
            # if the user didnt select a name it will fail.
            standartbox("Please select a name!", parent=self)
        else:
            box_first_name = str(self.CB_employee.currentText()).split()[0]
            user_return = standartbox(f"Enter a {self.quantname} to user {box_first_name}?", boxtype="okcancel", okstring="Yes", cancelstring="No", parent=self)
            # if the user return is ok (value 1024 in qt) then set the variable to carry on
            if user_return == 1024:
                enter_quant = True
        if enter_quant:
            # split the cb (since it displays first and lastname as onne)
            exist_employee = self.c.execute("SELECT COUNT(*) FROM employees WHERE first_name = ? and last_name = ?", (self.employee_first_name, self.employee_last_name)).fetchone()[0]
            if exist_employee:
                # also gets the time to insert into the tracking table, updates the label and checks if the user exceeded the critical amount of debts
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.c.execute("UPDATE OR IGNORE employees SET amount = amount + 1, money = money - ? WHERE ID = ?", (self.quantcosts, self.employee_id))
                self.c.execute("INSERT OR IGNORE INTO tracks(employee_ID, time) VALUES(?, ?)", (self.employee_id, time_now))
                self.DB.commit()
                money = self.c.execute("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
                self.update_money_shown(money, criticalcheck=True)
            else:
                # this should never happen
                standartbox("Ough! Somehow the employee doesn't exist in the Database!", parent=self)

    def pay_clicked(self):
        """ Gives the user the ability to pay his debts. """
        # checks if the employee name is given
        if self.employee_name == "":
            standartbox("No name selected!", parent=self)
        # select the id and in case of a critical error informs the user
        else:
            # This should also never happen since we will have a id with a selected employee
            if self.employee_id is None or not self.employee_id:
                standartbox("Sorry, something went wrong!", parent=self)
            else:
                # opens the paydialog window and passes id as well as name to it.
                self.paydialog = PayDialog(self)
                self.paydialog.showFullScreen()
    
    def options_clicked(self):
        """ Opens up the option dialog to chose different options and enter new users. """
        self.optiondialog = OptionDialog(self)
        self.optiondialog.showFullScreen()

    def combobox_change(self):
        """ Code gets called each time when the combobox is changed by a user or to refresh the money/debts. """
        # gets the new name of the employee
        employee_name = self.CB_employee.currentText()
        # only executes the code when the combobox is not empty
        if employee_name != "":
            first_name, last_name = employee_name.split()
            money, employee_id = self.c.execute("SELECT money, ID FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0:2]
            # sets the label according to the credit
            self.update_money_shown(money, criticalcheck=True)
            # updates the attributes of our class object (employee properties)
            self.employee_first_name = first_name
            self.employee_last_name = last_name
            self.employee_name = employee_name
            self.employee_id = employee_id
        else:
            self.L_money.setText("")
            self.L_paymentcall.setText("")
            # updates the attributes of our class object (employee properties)
            self.employee_first_name = ""
            self.employee_last_name = ""
            self.employee_name = ""
            self.employee_id = 0

    def lineedit_clicked(self, le_to_write, inputtype="kb", max_char_len=30, x_pos=150, y_pos=10, parent=None):
        """ Calls a keyboard/numpad to write text into a line edit.
        The mainwindow only got this method and inherits it to its children.

        arguments:

            -- le_to_write (obj): Lineedit were the input gets into
            -- Inputtype (str): "kb" for keyboard, "np" for numpad
            -- max_char_len (int): Limits the maximum chars
            -- x_pos (int): x-position of the numpad (left corner)
            -- y_pos (int): y-position of the numpad (left corner)
        """
        if parent is None:
            parent = self
        if inputtype == "kb":
            # print("Keyboard")
            parent.keyboard = KeyboardWidget(parent, le_to_write, max_char_len=max_char_len)
            parent.keyboard.showFullScreen()
        elif inputtype == "np":
            # print("numpad")
            parent.numpad = NumpadScreen(parent, x_pos=x_pos, y_pos=y_pos, le_to_write=le_to_write)
            parent.numpad.showMaximized()
            parent.numpad.move(x_pos, y_pos)

    def update_money_shown(self, money, criticalcheck=False):
        """ Updates the label in the mainscreen which shows the money.
        Only displays the critical warning at a coffe add (set to true), at other points it would get annoying.
        """
        # sets the label according to the credit
        prefix = ""
        if money < 0:
            prefix = "-"
        elif money > 0:
            prefix = "+"
        self.L_money.setText("{} {:.2f} €".format(prefix, abs(money)))
        # if the money exceeds a given value, then displays the payment call
        # the input is a positive number, since debts are negative we need to invert it!
        if (-1 * money) >= self.paymentcall_threshold:
            self.L_paymentcall.setText("please consider paying debts")
        else:
            self.L_paymentcall.setText("")
        #also checks the critical threshold if so prompts an message
        if (-1 * money) >= self.critical_threshold and criticalcheck:
            standartbox("You should really considering paying your debts! You slacker!!", parent=self)

    def lineedit_changed_number(self, le_object, max_decimals=2, max_text_length=2):
        """ Method to limit the lineedits entry to a set length/decimals"""
        le_text = le_object.text()
        # only works on numbers not some chars
        if le_text != "":
            try:
                le_value = float(le_text)
                # if the number is a int, it will stay an int
                if int(float(le_text)) == float(le_text):
                    le_value = int(le_text)
                # otherwise round it down to the given digits
                else:
                    le_value = int(le_value * 10**max_decimals)/10**max_decimals
                # if the value is too long ignore last entry
                if int(float(le_text)) >= 10**max_text_length:
                    le_value = le_text[:-1]
            except ValueError:
                le_value = le_text[:-1]
            # if there are no decimals, dots are not needed
            if max_decimals > 0:
                # the algorythm kills the dots so if the last digit is a dot just use the text and exclude more than one dot
                if le_text[-1] == "." and le_text.count(".")<2:
                    le_value = le_text
                # also need to check if after the dot is a zero, that the zero is not just converted away
                # this is a bandaid fix, in case of no decimal places it will cause problems so take that in consideration!
                if len(le_text)>1:
                    if le_text[-2] == "." and le_text[-1] == "0":
                        le_value = le_text
            le_object.setText(str(le_value))

    def fillenabled_combobox(self):
        """ Fills all enabled employees into the CB. """
        sqlstring = "SELECT first_name, last_name from employees WHERE enabled = 1 ORDER BY last_name ASC"
        self.CB_employee.addItem("")
        for employee in self.c.execute(sqlstring):
            self.CB_employee.addItem(" ".join((employee[0], employee[1])))


    def add_employee_clicked(self, first_name_object, last_name_object, update=False, id=None, checkbox_object=None):
        """ Adds the employee to the DB if not already exisiting and all Names are given and at least 3 chars. 
        Also got the possibility to change the the selected eployedd instead.
        """
        # replace all the spaces (we want only one first and one last name!)
        first_name = first_name_object.text().replace(" ","").capitalize() 
        last_name  = last_name_object.text().replace(" ","").capitalize() 
        # checks if any is empty or less than thress
        if first_name == "" or last_name == "":
            standartbox("At least one of the names is missing!", parent=self)
        elif len(first_name)<3 or len(last_name)<3:
            standartbox("The names need at least three character!", parent=self)
        else:
            # checks if already exists, else enter into the DB
            name_exists = self.c.execute("SELECT COUNT(*) FROM employees WHERE first_name = ? AND last_name = ?",(first_name, last_name)).fetchone()[0]
            if not name_exists and not update:
                self.c.execute("INSERT OR IGNORE INTO employees(first_name, last_name, amount, money, enabled) VALUES(?,?,0,0,1)",(first_name, last_name))
                self.DB.commit()
                first_name_object.clear()
                last_name_object.clear()
                standartbox("Employee {} {} was generated!".format(first_name, last_name), parent=self)
                self.CB_employee.addItem(" ".join((first_name, last_name)))
                self.CB_employee.model().sort(0)
            elif update:
                if checkbox_object.isChecked():
                    enabled = 1
                else:
                    enabled = 0
                self.c.execute("UPDATE OR IGNORE employees SET first_name=?, last_name=?, enabled=? WHERE ID=?",(first_name, last_name, enabled, id))
                self.DB.commit()
                self.CB_employee.clear()
                self.fillenabled_combobox()
                self.L_money.clear()
                standartbox("Employee {} {} was updated!".format(first_name, last_name), parent=self)
                return True
            else:
                standartbox("This employee already exists!", parent=self)
        return False