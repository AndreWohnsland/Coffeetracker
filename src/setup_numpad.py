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
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
            )
        self.setAttribute(Qt.WA_DeleteOnClose)
        # self.setWindowIcon(QIcon("Cocktail-icon.png"))
        # Connect all the buttons, generates a list of the numbers an objectnames to do that
        self.number_list = [x for x in range(10)]
        self.attribute_numbers = [getattr(self, "PB" + str(x)) for x in self.number_list]
        for obj, number in zip(self.attribute_numbers, self.number_list):
            obj.clicked.connect(lambda _, n=number: self.number_clicked(number=n))
        self.PBdot.clicked.connect(lambda: self.number_clicked(number="."))
        self.PBdel.clicked.connect(self.del_clicked)
        self.ms = parent
        if not self.ms.devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.pwlineedit = le_to_write
        self.move(x_pos, y_pos)

    def number_clicked(self, number):
        """  Adds the clicked number to the lineedit. """
        self.pwlineedit.setText(self.pwlineedit.text() + "{}".format(number))

    def del_clicked(self):
        """ Deletes the last digit in the lineedit. """
        if len(self.pwlineedit.text()) > 0:
            strstor = str(self.pwlineedit.text())
            self.pwlineedit.setText(strstor[:-1])