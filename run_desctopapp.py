import sys
import os
import sqlite3
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from desctop_ui.desctopdialog import Ui_DesctopMainWindow


class MainScreen(QMainWindow, Ui_DesctopMainWindow):
    """Creates the desctop application for the controlling in the desctop
    Currently uses most function out of the Pi programm, since the logic is similar.
    It is planned to connect via remote access to the DB and get all the data.
    """
    def __init__(self, parent=None, db_path=None):
        """ Init function for the MainWindow Class. """
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)

        # Connects to the DB
        if db_path is not None:
            self.DB = sqlite3.connect(db_path)
            self.c = self.DB.cursor()
        
        # some optical properties 
        self.setWindowIcon(QIcon('desctop_ui/coffee.png'))
        self.L_debts.setStyleSheet('color: rgb(0,0,0)')
        
        # Generates nececary variables
        self.employee_first_name = ""
        self.employee_last_name = ""
        self.employee_name = ""
        self.employee_id = 0
        self.emptystring = " -- select employee -- "

        # Connects all the CB
        self.CB_active.activated.connect(lambda: self.checkboxchange(mode='active', cb_object=self.CB_active))
        self.CB_modify.activated.connect(lambda: self.checkboxchange(mode='all', cb_object=self.CB_modify))

        # Connect all the Buttons
        self.PB_new.clicked.connect(lambda: self.add_employee(self.LE_firstname, self.LE_lastname))
        self.PB_default.clicked.connect(self.dummy)
        self.PB_pay.clicked.connect(self.pay_clicked)
        self.PB_plot_active.clicked.connect(lambda: self.plot_clicked(active=True))
        self.PB_plot_lifetime.clicked.connect(lambda: self.plot_clicked(active=False))
        self.PB_change.clicked.connect(lambda: self.add_employee(self.LE_modify_firstname, self.LE_modify_lastname, update=True, checkbox_object=self.CHB_active, combobox_object=self.CB_modify))

        # restrictions for the Lineedits
        max_char_len = 20
        regex = QRegExp("[a-zA-Z]+")
        validator = QRegExpValidator(regex)
        self.LE_firstname.setMaxLength(max_char_len)
        self.LE_firstname.setValidator(validator)
        self.LE_lastname.setMaxLength(max_char_len)
        self.LE_lastname.setValidator(validator)
        self.LE_modify_firstname.setMaxLength(max_char_len)
        self.LE_modify_firstname.setValidator(validator)
        self.LE_modify_lastname.setMaxLength(max_char_len)
        self.LE_modify_lastname.setValidator(validator)
        self.LE_payment.textChanged.connect(lambda: self.lineedit_changed_number(self.LE_payment))

        # assign the nececary values to the CB
        self.checkboxfill(mode='active', cb_object=self.CB_active)
        self.checkboxfill(cb_object=self.CB_modify)

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

    def dummy(self):
        pass

    def pay_clicked(self):
        """ First asks the user to proceed then enters the value into db. """
        enter_credit = False
        pay_amount = self.LE_payment.text()
        # Only carries on if a value is given
        if pay_amount == "":
            standartbox("No value to pay given!", parent=self)
        elif self.employee_id == 0:
            standartbox("No employee selected!", parent=self)
        else:
            # rounds the number down to two digits (best is to limit it even that way)
            pay_amount = round(float(pay_amount), 2)
            user_return = standartbox(f"Pay amount entered is: {pay_amount} €", boxtype="okcancel", okstring="Enter", parent=self)
            # if the user return is ok (value 1024 in qt) then set the variable to carry on
            if user_return == 1024:
                enter_credit = True
        # finally enters the data into the db and deletes the entry LE/ updates the label
        if enter_credit:
            self.c.execute("UPDATE OR IGNORE employees SET money = money + ? WHERE ID = ?",(pay_amount, self.employee_id))
            new_money = self.c.execute("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
            self.DB.commit()
            self.LE_payment.setText("")
            standartbox("Your payment has been entered!", parent=self)
            self.update_money_shown(new_money)

    def add_employee(self, first_name_object, last_name_object, update=False, emp_id=None, checkbox_object=None, combobox_object=None):
        """Adds the employee to the DB if not already exisiting and all Names are given and at least 3 chars. Also got the possibility to change the the selected eployedd instead.
        
        Args:
            first_name_object (qt_object): Lineedit for the first name
            last_name_object (qt_object): Lineedit for the last name
            update (bool, optional): Used if no new user but update old o. Defaults to False.
            id (int, optional): only used for update. Defaults to None.
            checkbox_object (qt_object, optional): Checkbox for the active/inactive feature. Defaults to None.
            combobox_object (qt_object, optional): Combobox for the active/inactive feature. Defaults to None.
        
        Returns:
            bool: State if the update could be carried out till the end
        """
        # replace all the spaces (we want only one first and one last name!)
        first_name = first_name_object.text().replace(" ","").capitalize() 
        last_name  = last_name_object.text().replace(" ","").capitalize() 
        # checks if any is empty or less than thress
        if update and combobox_object.currentText() == self.emptystring:
            standartbox("No name selected!", parent=self)
            return False
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
                standartbox(f"Employee {first_name} {last_name} was generated!", parent=self)
                self.CB_active.addItem(" ".join((first_name, last_name)))
                self.CB_active.model().sort(0)
                self.CB_modify.addItem(" ".join((first_name, last_name)))
                self.CB_active.model().sort(0)
            elif update:
                if checkbox_object.isChecked():
                    enabled = 1
                else:
                    enabled = 0
                emp_id = self.c.execute("SELECT ID FROM employees WHERE first_name=? AND last_name=?",(first_name, last_name)).fetchone()
                # if at the same time a user changes the entry, the search by name will not be successfull
                # for the future (if its possible) also assign the id to the DD and catch it with the id!
                if emp_id is None:
                    standartbox("Failed to get the old employee name, seems like someone just changed it, reloading dropdown... try again.", parent=self)
                    self.checkboxfill(mode='all', cb_object=self.CB_modify)
                else:
                    emp_id = emp_id[0]
                    self.c.execute("UPDATE OR IGNORE employees SET first_name=?, last_name=?, enabled=? WHERE ID=?",(first_name, last_name, enabled, emp_id))
                    self.DB.commit()
                    # clears an repopulates the CB // alternative here code to just replace or call to the function
                    self.checkboxfill(mode='all', cb_object=self.CB_modify)
                    self.checkboxfill(mode='active', cb_object=self.CB_active)
                    # resets all the other Ui elements
                    self.L_debts.setText("Balance:")
                    self.L_debts.setStyleSheet('color: rgb(0,0,0)')
                    first_name_object.clear()
                    last_name_object.clear()
                    self.CHB_active.setChecked(False)
                    standartbox(f"Employee {first_name} {last_name} was updated!", parent=self)
                    return True
            else:
                standartbox("This employee already exists!", parent=self)
        return False
    
    def plot_clicked(self, active=True):
        """ Plot a leaderboard of the best x employees. By best is ment the most entries. 
        Differentiates between all DB entries, and only still active employees.
        """
        # Selects the 5 employes with the highest comsumption either from all ore active
        if active:
            bonusstring = " WHERE enabled=1"
            headerstring="(active)"
        else:
            bonusstring = ""
            headerstring="(all time)"
        employee_data = self.c.execute(f"SELECT first_name, last_name, amount FROM employees{bonusstring} ORDER BY amount DESC LIMIT 5")
        namelist = []
        amountlist =  []
        # generates a list of the employees and values for later plotting, only picks up the five highest
        for row in employee_data:
            last_name = row[1]
            namelist.append(f"{row[0]} {last_name[0]}.")
            amountlist.append(row[2])
        # just for plotting the values of the output
        # print(20*"-")
        # for name, amount in zip(namelist, amountlist):
        #     print(name, amount)
        # opens up the window for the plot
        self.graphwindow = GraphWindow(self, plotvalues=amountlist[::-1], plotlabels=namelist[::-1], headerstring=headerstring)
        self.graphwindow.show()

    def checkboxfill(self, mode='all', cb_object=None):     
        """Refills the Comboboxes, either all names or just active ones.    
        
        Args:
            mode (str, optional): 'all' or 'active' to select according employees. Defaults to 'all'.
            cb_object (qt_object, optional): Needs to be given, the Comboboxobject to fill. Defaults to None.
        """
        if cb_object is None:
            raise ValueError("There needs to be an Combobox object to write to!")
        if mode == 'all':
            sql_bonus = ""
        elif mode =='active':
            sql_bonus = "WHERE enabled = 1 "
        else:
            raise ValueError("The mode have to be all or active!")
        sqlstring = f"SELECT first_name, last_name from employees {sql_bonus}ORDER BY last_name ASC"
        cb_object.clear()
        cb_object.addItem(self.emptystring)
        for employee in self.c.execute(sqlstring):
            cb_object.addItem(" ".join((employee[0], employee[1])))

    def checkboxchange(self, mode='all', cb_object=None):
        """Refills the Comboboxes, either all names or just active ones.    
        
        Args:
            mode (str, optional): 'all' or 'active' to select according employees. Defaults to 'all'.
            cb_object (qt_object, optional): Needs to be given, the Comboboxobject to fill. Defaults to None.
        """
        if cb_object is None:
            raise ValueError("There needs to be an Combobox object to write to!")
        if mode == 'all':
            employee_name = cb_object.currentText()
            if employee_name != self.emptystring:
                first_name, last_name = employee_name.split()
                emp_state = self.c.execute("SELECT enabled FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0]
                self.LE_modify_firstname.setText(first_name)
                self.LE_modify_lastname.setText(last_name)
                if emp_state:
                    self.CHB_active.setChecked(True)
                else:
                    self.CHB_active.setChecked(False)
            else:
                self.LE_modify_firstname.setText("")
                self.LE_modify_lastname.setText("")
                self.CHB_active.setChecked(False)
        elif mode =='active':
            employee_name = cb_object.currentText()
            # only executes the code when the combobox is not empty
            if employee_name != self.emptystring:
                first_name, last_name = employee_name.split()
                money, employee_id = self.c.execute("SELECT money, ID FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0:2]
                # sets the label according to the credit
                self.update_money_shown(money)
                # updates the attributes of our class object (employee properties)
                self.employee_first_name = first_name
                self.employee_last_name = last_name
                self.employee_name = employee_name
                self.employee_id = employee_id
            else:
                self.L_debts.setText("Balance:")
                self.L_debts.setStyleSheet('color: rgb(0,0,0)')
                # updates the attributes of our class object (employee properties)
                self.employee_first_name = ""
                self.employee_last_name = ""
                self.employee_name = ""
                self.employee_id = 0
        else:
            raise ValueError("The mode have to be all or active!")


    def update_money_shown(self, money):
        """Updates the label in the mainscreen which shows the money."""
        # sets the label according to the credit
        prefix = ""
        if money < 0:
            prefix = "-"
            self.L_debts.setStyleSheet('color: rgb(255, 0, 0)')
        elif money > 0:
            prefix = "+"
            self.L_debts.setStyleSheet('color: rgb(34,139,34)')
        self.L_debts.setText(f"Balance:  {prefix} {abs(money):.2f} €")

class GraphWindow(QDialog):
    """
    Opens up a window where the the top five useres (highes quantity) are shown.

    Parameters:
        -- plotvalues: The values for the bars
        -- plotlabels: The labels for the bars
        -- headerstring: Depreciated, renames the window titel, is not shown anymore in fullscreen
    """
    def __init__(self, parent, plotvalues=None, plotlabels=None, headerstring="all time"):
        super(GraphWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        self.setWindowTitle("Leaderboard {}".format(headerstring))
        # self.setModal(True)
        self.ms = parent

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(3, 1.5), dpi=200)
        # adds a button to go back
        self.backbutton = QPushButton('< Back')
        # sets the minimum size and the fontsize
        self.backbutton.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backbutton.setFont(font)
        self.backbutton.clicked.connect(self.back_clicked)
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.backbutton)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # clears the old values and then adds a subplot to isert all the data
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # plots a horizontal bargraph with the values and the namelabels
        y_pos = np.arange(len(plotlabels))
        ax.xaxis.grid(linestyle='--', color='w', zorder=0)
        # generates a color grade from red to blue
        clist = [(0, '#1f77b4'), (1, '#d62728')]
        rvb = mcolors.LinearSegmentedColormap.from_list("", clist)
        ax.barh(y_pos, plotvalues, tick_label=plotlabels, zorder=3, height=0.9, color=rvb(y_pos/len(plotlabels)))
        # gets the numbers in front of each bar
        for i, v in enumerate(plotvalues):
            ax.text(max(plotvalues)/50, i-0.05, str(v), color='w', fontweight='bold', va='center', fontsize=10)
        # removes the ticks from each axis
        for ticx in ax.xaxis.get_major_ticks():
            ticx.tick1line.set_visible(False)
            ticx.tick2line.set_visible(False)
        for ticy in ax.yaxis.get_major_ticks():
            ticy.tick1line.set_visible(False)
            ticy.tick2line.set_visible(False)
        # recolours the style into invers (black is white, white is black)
        self.figure.patch.set_facecolor('k')
        ax.patch.set_facecolor('k')
        ax.spines['bottom'].set_color('w')
        ax.spines['top'].set_color('w')
        ax.spines['left'].set_color('w')
        ax.spines['right'].set_color('w')
        plt.setp(ax.get_xticklabels(), color="w", fontsize=8)
        plt.setp(ax.get_yticklabels(), color="w", fontsize=8)
        plt.tight_layout()
        # refresh canvas
        self.canvas.draw()

    def back_clicked(self):
        """ Closes the window. """
        self.close()

def standartbox(textstring, boxtype="standard", okstring="OK", cancelstring="Cancel", parent=None):
    """ The default messagebox for the Maker. Uses a QMessageBox with OK-Button 
    Boxtypes are:
        standard: Only an ok button and a text
        okcancel: Text with option to okay or cancel 
    """
    # print(textstring)
    msgBox = QMessageBox(parent)
    if boxtype == "standard":
        msgBox.setStandardButtons(QMessageBox.Ok)   
        msgBox.setWindowTitle("Coffeetracker - Info")
        msgBox.setIcon(QMessageBox.Information)
    elif boxtype == "okcancel":
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        buttoncancel = msgBox.button(QMessageBox.Cancel)
        buttoncancel.setText("{: ^12}".format(cancelstring))
        msgBox.setWindowTitle("Coffeetracker - Selection")
        msgBox.setIcon(QMessageBox.Question)
    buttonok = msgBox.button(QMessageBox.Ok)
    buttonok.setText("{: ^12}".format(okstring))
    fillstring = "-" * 40
    fillstring = ""
    msgBox.setText("{0}\n{1}\n{0}".format(fillstring, textstring))
    msgBox.setWindowIcon(QIcon('desctop_ui/coffee.png'))
    msgBox.show()
    retval = msgBox.exec_()
    if boxtype == "okcancel":
        # print("value of pressed message box button:", retval)
        return retval

db_name = "employees_dummy"    
paymentcall_threshold = 10      # When the pay message got displayed (critical is 1.5 that value)
quantcosts = 0.25               # cost of one quant (can also be 0)
quantname = "coffee"            # name of your quants

# path gerneration for the DB
subfoldername = "data"
dirpath = os.path.dirname(__file__)
db_path = os.path.join(dirpath, subfoldername, "{}.db".format(db_name))

if __name__ == "__main__":
    # creates the application
    app = QApplication(sys.argv)
    #creates the mainscreen, sets it to fixed size and fullscreen
    w = MainScreen(db_path=db_path)
    w.show()
    # runs the app until the exit
    sys.exit(app.exec_())