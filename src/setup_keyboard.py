import sys
import string

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from ui_elements.keyboard import Ui_Keyboard


class KeyboardWidget(QDialog, Ui_Keyboard):
    """ Creates a Keyboard where the user can enter names or similar strings to Lineedits. 
        
    arguments:
        -- le_to_write (obj): Lineedit were the input gets into
        -- max_char_len (int): Limits the maximum chars
    """

    def __init__(self, parent, le_to_write=None, max_char_len=30):
        super(KeyboardWidget, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ms = parent
        self.devenvironment = self.ms.devenvironment
        if not self.devenvironment:
            self.setCursor(Qt.BlankCursor)
        self.le_to_write = le_to_write
        self.LName.setText(self.le_to_write.text())
        # populating all the buttons
        self.backButton.clicked.connect(self.backbutton_clicked)
        self.clear.clicked.connect(self.clearbutton_clicked)
        self.enterButton.clicked.connect(self.enterbutton_clicked)
        # self.space.clicked.connect(lambda: self.inputbutton_clicked(" ", " "))
        self.dotButton.clicked.connect(lambda: self.inputbutton_clicked(".", "."))
        self.delButton.clicked.connect(self.delete_clicked)
        self.shift.clicked.connect(self.shift_clicked)
        # generating the lists to populate all remaining buttons via iteration
        self.char_list_lower = [x for x in string.ascii_lowercase]
        self.char_list_upper = [x for x in string.ascii_uppercase]
        self.attribute_chars = [getattr(self, "Button" + x) for x in self.char_list_lower]
        for obj, char, char2 in zip(self.attribute_chars, self.char_list_lower, self.char_list_upper):
            obj.clicked.connect(lambda _, iv=char, iv_s=char2: self.inputbutton_clicked(inputvalue=iv, inputvalue_shift=iv_s))
        # self.number_list = [x for x in range(10)]
        # self.attribute_numbers = [getattr(self, "Button" + str(x)) for x in self.number_list]
        # for obj, char, char2 in zip(self.attribute_numbers, self.number_list, self.number_list):
        #     obj.clicked.connect(lambda _, iv=char, iv_s=char2: self.inputbutton_clicked(inputvalue=iv, inputvalue_shift=iv_s))
        # restricting the Lineedit to a set up Char leng
        self.LName.setMaxLength(max_char_len)

    def backbutton_clicked(self):
        """ Closes the Window without any further action. """
        self.close()
    
    def clearbutton_clicked(self):
        """ Clears the input. """
        self.LName.setText("")

    def enterbutton_clicked(self):
        """ Closes and enters the String value back to the Lineedit. """
        self.le_to_write.setText(self.LName.text())
        self.close()

    def inputbutton_clicked(self, inputvalue, inputvalue_shift):
        """ Enters the inputvalue into the field, adds it to the string.
        Can either have the normal or the shift value, if there is no difference both imput arguments are the same.
        """
        stringvalue = self.LName.text()
        if self.shift.isChecked():
            addvalue = inputvalue_shift
        else:
            addvalue = inputvalue
        stringvalue += str(addvalue)
        self.LName.setText(stringvalue)

    def delete_clicked(self):
        stringvalue = self.LName.text()
        if len(stringvalue) > 0:
            self.LName.setText(stringvalue[:-1])

    def shift_clicked(self):
        if self.shift.isChecked():
            charchoose = self.char_list_upper
        else:
            charchoose = self.char_list_lower
        for obj, char in zip(self.attribute_chars, charchoose):
            obj.setText(str(char))