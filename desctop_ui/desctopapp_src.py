import sys
import os
import sqlite3
import datetime
import configparser
import pysftp
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
from desctop_ui.configdialog import Ui_ConfigDialog


class MainScreen(QMainWindow, Ui_DesctopMainWindow):
    """Creates the desctop application for the controlling in the desctop
    Currently uses most function out of the Pi programm, since the logic is similar.
    It is planned to connect via remote access to the DB and get all the data.
    Needs a path to the DB, quantname and quantcosts if wished
    The dirpath is the absolute path where the main is running. Currently unused.
    """
    def __init__(self, parent=None, db_path=None, quantname="Coffee", quantcosts=0.25, dirpath=''):
        """ Init function for the MainWindow Class. """
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)

        # Gets the DB path and the configs
        self.db_path = db_path
        config = configparser.ConfigParser()
        self.employeeconfig_path = 'employeeconfig.ini'
        config.read(self.employeeconfig_path)
        self.default_firstname = config['employee']['firstname']
        self.default_lastname = config['employee']['lastname']
        self.default_empid = int(config['employee']['empid'])
        self.db_location, self.db_type, self.pi_ip, self.pi_name, self.pi_password = get_config()
        self.pi_db_filepath, self.pi_quant_filepath, self.local_db_filepath, self.local_quant_filepath = generate_filepath(self.db_type)

        # Generates nececary variables
        self.employee_first_name = ""
        self.employee_last_name = ""
        self.employee_name = ""
        self.employee_id = 0
        self.emptystring = " -- select employee -- "
        self.quantcosts = quantcosts
        self.quantname = quantname

        # some optical properties 
        self.setWindowIcon(QIcon('desctop_ui/coffee.png'))
        self.L_debts.setStyleSheet('color: rgb(0,0,0)')
        self.PB_add_coffee.setText(f"Add {self.quantname}")
        self.label_8.setText(f"Payment, {self.quantname.capitalize()} and Plots")
        self.label_5.setText(f"Add {self.quantname}, pay debts\nor just plot stuff for fun")

        # Connects all the CB
        self.CB_active.activated.connect(lambda: self.comboboxchange(mode='active', cb_object=self.CB_active))
        self.CB_modify.activated.connect(lambda: self.comboboxchange(mode='all', cb_object=self.CB_modify))

        # Connect all the Buttons
        self.PB_new.clicked.connect(lambda: self.add_employee(self.LE_firstname, self.LE_lastname))
        self.PB_default.clicked.connect(self.set_config)
        self.PB_pay.clicked.connect(self.pay_clicked)
        self.PB_add_coffee.clicked.connect(self.add_coffee)
        self.PB_undo.clicked.connect(self.undo_last)
        self.PB_plot.clicked.connect(self.plot_clicked)
        self.PB_change.clicked.connect(lambda: self.add_employee(self.LE_modify_firstname, self.LE_modify_lastname, update=True, checkbox_object=self.CHB_active, combobox_object=self.CB_modify))

        # Connects the menu
        self.actionTodo.triggered.connect(self.action_what)
        self.actionAbout.triggered.connect(self.action_about)
        self.actionExit.triggered.connect(self.action_exit)
        self.actionCofigure_con.triggered.connect(self.action_configure)

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
        self.comboboxfill(mode='active', cb_object=self.CB_active)
        self.comboboxfill(cb_object=self.CB_modify)

        # gets the default entry for the CB
        self.set_default()

    def lineedit_changed_number(self, le_object, max_decimals=2, max_text_length=2):
        """Method to limit the lineedits entry to a set length/decimals
        
        Args:
            le_object (qt_object): Lineedit connected to that function
            max_decimals (int, optional): Number of decimals. Defaults to 2.
            max_text_length (int, optional): Amount of number before the dot (2 for max 99.). Defaults to 2.
        """
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
        """ Dummy to fill some connection before using them. """
        pass

    def set_config(self):
        """ Changes the default config settings to the selected user. """
        # connects to the user specific config (each user can have different ones)
        config = configparser.ConfigParser()
        config.read(self.employeeconfig_path)
        # saves name and id into the config
        config['employee']['firstname'] = f'{self.employee_first_name}'
        config['employee']['lastname'] = f'{self.employee_last_name}'
        config['employee']['empid'] = f'{self.employee_id}'
        # writes the file, update the class properties accordingly
        with open(self.employeeconfig_path, 'w') as configfile:
            config.write(configfile)
        self.default_firstname = self.employee_first_name
        self.default_lastname = self.employee_last_name
        self.default_empid = self.employee_id
        standartbox(f"The User {self.employee_first_name} {self.employee_last_name} was set as default.", parent=self)

    def pay_clicked(self):
        """ First asks the user to proceed then enters the value into db. """
        enter_credit = False
        pay_amount = self.LE_payment.text()
        # Only carries on if a value is given and a employee is selected
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
            self.infobox("~~ Updating data on pi ~~", "Downloading and uploading the data on the pi, please wait", self)
            self.queryDB("UPDATE OR IGNORE employees SET money = money + ? WHERE ID = ?",(pay_amount, self.employee_id))
            self.msgBox.close()
            new_money = self.queryDB("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
            self.LE_payment.setText("")
            standartbox("Your payment has been entered!", parent=self)
            self.update_money_shown(new_money)

    def add_coffee(self):
        """ Adds one quantity to the employee. """
        # if there is an employee selected, gets the first and the last name and search into the db, insert the values
        enter_quant = False
        if self.employee_first_name == "":
            # if the user didnt select a name it will fail.
            standartbox("Please select a name!", parent=self)
        else:
            box_first_name = str(self.CB_active.currentText()).split()[0]
            user_return = standartbox(f"Enter a {self.quantname} to user {box_first_name}?", boxtype="okcancel", okstring="Yes", cancelstring="No", parent=self)
            # if the user return is ok (value 1024 in qt) then set the variable to carry on
            if user_return == 1024:
                enter_quant = True
        if enter_quant:
            # split the cb (since it displays first and lastname as onne)
            exist_employee = self.queryDB("SELECT COUNT(*) FROM employees WHERE ID = ?", (self.employee_id,)).fetchone()[0]
            if exist_employee:
                # also gets the time to insert into the tracking table, updates the label and checks if the user exceeded the critical amount of debts
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.infobox("~~ Updating data on pi ~~", "Downloading and uploading the data on the pi, please wait", self)
                self.queryDB("UPDATE OR IGNORE employees SET amount = amount + 1, money = money - ? WHERE ID = ?", (self.quantcosts, self.employee_id))
                self.queryDB("INSERT OR IGNORE INTO tracks(employee_ID, time) VALUES(?, ?)", (self.employee_id, time_now))
                money = self.queryDB("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
                self.msgBox.close()
                self.update_money_shown(money)
            else:
                # this should never happen
                standartbox("Ough! Somehow the employee doesn't exist in the Database!", parent=self)

    def undo_last(self):
        """ Undo the last quantity entry. It just removes one time payment and amount from the list """
        # asks the user if he wants to remove his last entry, if so, carries on in the process
        # needs also to check that a employee is selected
        if self.CB_active != self.emptystring:
            user_return = standartbox(f"Remove the last entry for {self.employee_first_name} {self.employee_last_name}?", boxtype="okcancel", okstring="Yes", cancelstring="No", parent=self)
        else:
            user_return = 0
        if user_return == 1024:
            current_money = self.queryDB("SELECT money FROM employees WHERE ID = ?",(self.employee_id,)).fetchone()[0]
            new_money = current_money + self.quantcosts
            self.infobox("~~ Updating data on pi ~~", "Downloading and uploading the data on the pi, please wait", self)
            self.queryDB("UPDATE OR IGNORE employees SET money = ?, amount = amount - 1 WHERE ID = ?",(new_money, self.employee_id))
            # deletes the last entry of the employee in the tracking list
            self.queryDB("DELETE FROM tracks WHERE Number=(SELECT max(Number) FROM tracks WHERE employee_ID=?)",(self.employee_id,))
            self.msgBox.close()
            # sets the label according to the credit
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
            # checks if already exists, else enter into the DB and updates the Comboboxes/sorts them
            name_exists = self.queryDB("SELECT COUNT(*) FROM employees WHERE first_name = ? AND last_name = ?",(first_name, last_name)).fetchone()[0]
            if not name_exists and not update:
                self.infobox("~~ Updating data on pi ~~", "Downloading and uploading the data on the pi, please wait", self)
                self.queryDB("INSERT OR IGNORE INTO employees(first_name, last_name, amount, money, enabled) VALUES(?,?,0,0,1)",(first_name, last_name))
                self.msgBox.close()
                first_name_object.clear()
                last_name_object.clear()
                standartbox(f"Employee {first_name} {last_name} was generated!", parent=self)
                self.comboboxfill(mode='all', cb_object=self.CB_modify)
                self.comboboxfill(mode='active', cb_object=self.CB_active)
                self.set_default()
            elif update:
                if checkbox_object.isChecked():
                    enabled = 1
                else:
                    enabled = 0
                emp_id = self.CB_modify.currentData()
                self.infobox("~~ Updating data on pi ~~", "Downloading and uploading the data on the pi, please wait", self)
                self.queryDB("UPDATE OR IGNORE employees SET first_name=?, last_name=?, enabled=? WHERE ID=?",(first_name, last_name, enabled, emp_id))
                self.msgBox.close()
                # clears an repopulates the CB // alternative here code to just replace or call to the function
                self.comboboxfill(mode='all', cb_object=self.CB_modify)
                self.comboboxfill(mode='active', cb_object=self.CB_active)
                # resets all the other Ui elements
                self.L_debts.setText("Balance:")
                self.L_debts.setStyleSheet('color: rgb(0,0,0)')
                self.set_default()
                first_name_object.clear()
                last_name_object.clear()
                self.CHB_active.setChecked(False)
                standartbox(f"Employee {first_name} {last_name} was updated!", parent=self)
                return True
            else:
                standartbox("This employee already exists!", parent=self)
        return False
    
    def plot_clicked(self, active=True):
        """Plot a leaderboard of the best x employees. By best is ment the most entries. 
        Differentiates between all DB entries, and only still active employees.
        
        Args:
            active (bool, optional): Decidor for only active employees or all. Defaults to True.
        """
        # Selects the 5 employes with the highest comsumption either from all ore active
        user_return = standartbox("Select only active employees or all ever existing ones?", boxtype="okcancel", okstring="active", cancelstring="all", parent=self)
        if user_return == 1024:
            bonusstring = " WHERE enabled=1"
            headerstring="(active)"
        else:
            bonusstring = ""
            headerstring="(all time)"
        employee_data = self.queryDB(f"SELECT first_name, last_name, amount FROM employees{bonusstring} ORDER BY amount DESC LIMIT 5")
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

    def comboboxfill(self, mode='all', cb_object=None):     
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
        sqlstring = f"SELECT first_name, last_name, ID from employees {sql_bonus}ORDER BY last_name ASC"
        cb_object.clear()
        cb_object.addItem(self.emptystring, 0)
        # adds all selected employees, as well as their id to the CB
        employeelist = self.queryDB(sqlstring).fetchall()
        for employee in employeelist:
            cb_object.addItem(" ".join((employee[0], employee[1])), employee[2])

    def comboboxchange(self, mode='all', cb_object=None):
        """Fils the Lineedits, and write the values to them    
        
        Args:
            mode (str, optional): 'all' or 'active' to select according employees. Defaults to 'all'.
            cb_object (qt_object, optional): Needs to be given, the Comboboxobject to fill. Defaults to None.
        """
        if cb_object is None:
            raise ValueError("There needs to be an Combobox object to write to!")
        # first checks if there was any change in naming from another user in the meantime (multiple user can acess so this can happen)
        # still needs to investigate if cb can have multiple values (shown and intern values) then set intern to id and shown to name!
        go_on = True
        employee_name = cb_object.currentText()
        employee_id = cb_object.currentData()
        # only carries out if there is a selection
        if employee_name != self.emptystring:
            first_name, last_name = cb_object.currentText().split()
            emp_id = self.queryDB("SELECT ID FROM employees WHERE first_name=? AND last_name=?",(first_name, last_name)).fetchone()
            # in any case of not getting the id refreshes the boxes and informs the user
            if emp_id is None:
                standartbox("Failed to get the old employee name, seems like someone just changed it, reloading dropdown... try again.", parent=self)
                self.comboboxfill(mode='all', cb_object=self.CB_modify)
                self.comboboxfill(mode='active', cb_object=self.CB_active)
                go_on = False
        if not go_on:
            pass
        elif mode == 'all':
            if employee_name != self.emptystring:
                # gets the enabloed status and the names for the Master dialog
                first_name, last_name = employee_name.split()
                emp_state = self.queryDB("SELECT enabled FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0]
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
            # only executes the code when the combobox is not empty
            if employee_name != self.emptystring:
                # Updates the Label and the Class properties
                first_name, last_name = employee_name.split()
                money, employee_id = self.queryDB("SELECT money, ID FROM employees WHERE first_name = ? and last_name = ?", (first_name, last_name)).fetchone()[0:2]
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
        """Updates the label in the mainscreen which shows the money.
        
        Args:
            money (float): Value for the Balance.
        """
        # sets the label according to the credit
        prefix = ""
        if money < 0:
            prefix = "-"
            self.L_debts.setStyleSheet('color: rgb(255, 0, 0)')
        elif money > 0:
            prefix = "+"
            self.L_debts.setStyleSheet('color: rgb(34,139,34)')
        self.L_debts.setText(f"Balance:  {prefix} {abs(money):.2f} €")

    def set_default(self):
        """ Updates the combobox to the default user"""
        if self.default_empid != 0:
            naming = self.queryDB("SELECT first_name, last_name FROM employees WHERE ID = ?", (self.default_empid,)).fetchone()
            if naming is not None:
                search_cb = " ".join((naming[0], naming[1]))
                index = self.CB_active.findText(search_cb, Qt.MatchFixedString)
                self.CB_active.setCurrentIndex(index)
        self.comboboxchange(mode='active', cb_object=self.CB_active)

    def get_database(self):
        """ Gets the path to the database. If its extern, copies it to the local file. """
        # self.pi_db_filepath, self.pi_quant_filepath, self.local_db_filepath, self.local_quant_filepath
        if self.db_location == 'pi':
            try:
                cnopts = pysftp.CnOpts()
                cnopts.hostkeys = None
                with pysftp.Connection(self.pi_ip, username=self.pi_name, password=self.pi_password, cnopts=cnopts) as sftp:
                    sftp.get(self.pi_db_filepath, self.local_db_filepath)
            except:
                standartbox("Could not Connect to the Pi! Please check if the Pi is turned on and connected to the Network!")
                self.close()
        

    def put_database(self):
        """ Puts the modified DB back to the Pi. """
        if self.db_location == 'pi':
            try:
                cnopts = pysftp.CnOpts()
                cnopts.hostkeys = None
                with pysftp.Connection(self.pi_ip, username=self.pi_name, password=self.pi_password, cnopts=cnopts) as sftp:
                    sftp.put(self.local_db_filepath, self.pi_db_filepath)
            except:
                standartbox("Could not Connect to the Pi! Please check if the Pi is turned on and connected to the Network!")
                self.close()

    def connDB(self):
        """Connect to the database and generates a cursor
        """
        self.DB = sqlite3.connect(self.db_path)
        self.c = self.DB.cursor()

    def queryDB(self, sql, serachtuple=()):
        """Executes the sql querry, closes the connection afterwards.
        
        Args:
            sql (str): Sql String to execute
            serachtuple (tuple): Aditional arguments to search for
        
        Returns:
            cursor: Data (tuple or None) if a select statement was chosen
        """
        if sql[0:6].lower() != 'select':
            self.DB.close()
            self.get_database()

        self.connDB()
        self.c.execute(sql, serachtuple)

        if sql[0:6].lower() == 'select':
            result = self.c
            return result
        else:
            self.DB.commit()
            self.DB.close()
            self.put_database()
            
    def infobox(self, title=None, text=None, parent=None):
        self.msgBox = QMessageBox(parent)
        self.msgBox.setWindowTitle(title)
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(text)
        self.msgBox.setWindowIcon(QIcon('desctop_ui/coffee.png'))
        self.msgBox.show()
        # retval = self.msgBox.exec_()

    def action_what(self):
        """ Short info message for the user what to do. """
        standartbox(f"This app is all about managing {self.quantname}! You can add a quantity, pay your debts, plot the user with the most or add/change users.")

    def action_about(self):
        """ Short info message about this application. """
        standartbox("This app was programmed by Andre Wohnsland. For further information see: https://github.com/AndreWohnsland/Coffeetracker.")

    def action_exit(self):
        """ Close action for the bar. """
        self.close()

    def action_configure(self):
        """ Generation for the Configuration. Guides the user through the configuration.
        Also gets called if the app starts the first time (the config.ini holds this information)
        """
        self.configurewindow = ConfigDialog(self)
        self.configurewindow.show()

class GraphWindow(QDialog):
    """
    Opens up a window where the the top five useres (highes quantity) are shown.

    Parameters:
        -- plotvalues: The values for the bars
        -- plotlabels: The labels for the bars
        -- headerstring: Depreciated, renames the window titel, is not shown anymore in fullscreen
    """
    def __init__(self, parent, plotvalues=None, plotlabels=None, headerstring="all time"):
        """ Generates the window and plots the diagram. """
        super(GraphWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        self.setWindowTitle("Leaderboard {}".format(headerstring))
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
            )
        # self.setModal(True)
        self.ms = parent

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(3, 1.5), dpi=220)
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

class ConfigDialog(QDialog, Ui_ConfigDialog):
    """ """
    def __init__(self, parent):
        """ Init function for the Configdialog Class. """
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.ms = parent
        self.employeeconfig_path = self.ms.employeeconfig_path
        # get the config data and assign the values accordingly
        self.location, self.db_type, self.pi_ip, self.pi_name, self.pi_password = get_config()
        if self.location == 'pi':
            self.RB_pi.setChecked(True)
        if self.db_type == 'own':
            self.RB_own.setChecked(True)
        self.LE_ip.setText(self.pi_ip)
        self.LE_name.setText(self.pi_name)
        self.LE_password.setText(self.pi_password)

        # connects the buttons
        self.PB_change.clicked.connect(self.change_config)
        self.PB_cancel.clicked.connect(lambda: self.close())

    def change_config(self):
        """ Evaluates the data and if everything is okay enters it into the """
        # first checks if its the pi, that everythin is given
        if self.RB_pi.isChecked() and (self.LE_ip.text()=="" or self.LE_name.text()=="" or self.LE_password.text()==""):
            standartbox("At least one entry for the pi is missing", parent=self)
        # elif self.RB_pi.isChecked():
        #     print("Check if the data is valid or not")
        # if no errors, go on
        else:
            config = configparser.ConfigParser()
            user_path = self.employeeconfig_path
            config.read(user_path)
            # checks if the pi or local and own or dummy data, saves the information
            if self.RB_pi.isChecked():
                config['program']['db_location'] = 'pi'
                config['pi']['ip'] = self.LE_ip.text()
                config['pi']['name'] = self.LE_name.text()
                config['pi']['password'] = self.LE_password.text()
            else:
                config['program']['db_location'] = 'local'
            if self.RB_own.isChecked():
                config['program']['db_type'] = 'own'
            else:
                config['program']['db_type'] = 'dummy'
            # finally writes all the information
            with open(user_path, 'w') as configfile:
                config.write(configfile)
            standartbox("The config was changed ... closing the program ... please start again.", parent=self)
            self.close()
            self.ms.close()

def standartbox(textstring, boxtype="standard", okstring="OK", cancelstring="Cancel", parent=None):
    """The default messagebox for the Maker. Uses a QMessageBox with OK-Button 
    
    Args:
        textstring (str): Display message for the box.
        boxtype (str, optional): Type of the dialog. Use standard or okcancel. Defaults to "standard".
        okstring (str, optional): Label of the ok-Button. Defaults to "OK".
        cancelstring (str, optional): Label ob the cancel (or other) button. Defaults to "Cancel".
        parent (qt_window, optional): Parent qt window from where the dialog should inherit the style/properties. Defaults to None.
    
    Returns:
        int: Boxvalue, specific to the qt Framework, 1024 for ok clicked.
    """
    # Boxtypes are:
    #     standard: Only an ok button and a text
    #     okcancel: Text with option to okay or cancel 
    # 
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

def get_properties(src_path, path_not_found=False):
    """Reads the single properties for the quantities and the propramm out of the according .ini files.
    Later also a synchronisation from the machine properties is planned.
    
    Args:
        src_path (str): Path to the runme python file
        path_not_found (Bool): Rerun this method with true if the db on pi was not found to get local values instead. Defaults to False.
    
    Returns:
        tuple: tuple of properties: Database path, threshold value, quantcosts, quantname, error during handling the process
    """
    # reads the user definited configs
    handling_error = False
    config_quant = configparser.ConfigParser()
    # gets all the properties out of the ini file
    master_location, db_type, pi_ip, pi_name, pi_password = get_config()
    # generates the name of the DB (dummy or not)
    pi_db_filepath, pi_quant_filepath, local_db_filepath, local_quant_filepath = generate_filepath(db_type)

    if path_not_found:
        master_location = 'local'

    # if the db is remote on the pi, checks if the connection is possible, otherwise return an error.
    # here os.path.isfile should be the key function to establish the connection check!
    # also consult https://stackoverflow.com/questions/12932607/how-to-check-if-a-sqlite3-database-exists-in-python for further information
    # or https://www.guru99.com/python-check-if-file-exists.html
    # for me: this will probably not take place here, but mostly in the other method in the mainclass. get and put of the db b4 and after sql inserts
    if master_location == 'pi':
        try:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            with pysftp.Connection(pi_ip, username=pi_name, password=pi_password, cnopts=cnopts) as sftp:
                sftp.get(pi_db_filepath, local_db_filepath)
                sftp.get(pi_quant_filepath, local_quant_filepath)
        except:
            return (None, None, None, None, True)
    # connects to the ini with the quant data
    config_quant.read(local_quant_filepath)
    threshold = float(config_quant['properties']['paymentcall_threshold'])
    quantcosts = float(config_quant['properties']['quantcosts'])
    quantname = str(config_quant['properties']['quantname']).replace('"','')
    return (local_db_filepath, threshold, quantcosts, quantname, handling_error)

def get_config():
    config = configparser.ConfigParser()
    user_path = "employeeconfig.ini"
    config.read(user_path)
    location = config['program']['db_location']
    db_type = config['program']['db_type']
    pi_ip = config['pi']['ip']
    pi_name = config['pi']['name']
    pi_password = config['pi']['password']
    return (location, db_type, pi_ip, pi_name, pi_password)


def generate_filepath(db_type):
    """ Generates all the paths to the pi and to the pc for db and ini files."""
    # generates the name of the DB (dummy or not)
    suffix_db = ""
    if db_type == 'dummy':
        suffix_db = "_dummy"
    db_filename = f"employees{suffix_db}.db"
    # generates the path to the properties and the db (local or pi)
    # generates the path to the pi and to the local file
    pi_db_filepath = f"/home/pi/Coffeetracker/data/{db_filename}"
    pi_quant_filepath = "/home/pi/Coffeetracker/quantconfig.ini"
    local_db_filepath = f"data/{db_filename}"
    local_quant_filepath = "quantconfig.ini" 
    return (pi_db_filepath, pi_quant_filepath, local_db_filepath, local_quant_filepath)