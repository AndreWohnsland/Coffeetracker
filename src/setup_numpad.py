import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.numpad import Ui_numpadwindow


class NumpadScreen(QDialog, Ui_numpadwindow):
    """ Creates the NumpadScreen. 
    
    arguments:
        -- le_to_write (obj): Lineedit were the input gets into
        -- x_pos (int): x-position of the numpad (left corner)
        -- y_pos (int): y-position of the numpad (left corner)
    """

    def __init__(self, parent, x_pos=0, y_pos=0, le_to_write=None):
        """ Init. Connect all the buttons and set window policy. """
        super(NumpadScreen, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.LE_money.setText(le_to_write.text())
        self.le_to_write = le_to_write
        # self.setWindowIcon(QIcon("Cocktail-icon.png"))
        # Connect all the buttons, generates a list of the numbers an objectnames to do that
        self.number_list = [x for x in range(10)]
        self.attribute_numbers = [getattr(self, "PB" + str(x)) for x in self.number_list]
        for obj, number in zip(self.attribute_numbers, self.number_list):
            obj.clicked.connect(lambda _, n=number: self.number_clicked(number=n))
        self.PBdot.clicked.connect(lambda: self.number_clicked(number="."))
        self.PBdel.clicked.connect(self.del_clicked)
        self.PB_cancel.clicked.connect(self.cancel_clicked)
        self.PB_ok.clicked.connect(self.enter_clicked)
        self.LE_money.textChanged.connect(lambda: self.ms.lineedit_changed_number(self.LE_money))
        # self.move(self.x_pos, self.y_pos)

    def number_clicked(self, number):
        """  Adds the clicked number to the lineedit. """
        self.LE_money.setText(self.LE_money.text() + "{}".format(number))

    def del_clicked(self):
        """ Deletes the last digit in the lineedit. """
        if len(self.LE_money.text()) > 0:
            strstor = str(self.LE_money.text())
            self.LE_money.setText(strstor[:-1])

    def enter_clicked(self):
        self.le_to_write.setText(self.LE_money.text())
        self.close()

    def cancel_clicked(self):
        self.close()
