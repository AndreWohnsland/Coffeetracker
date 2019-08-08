import sys
import os
import configparser

from PyQt5.QtWidgets import QApplication

from desctop_ui.desctopapp_src import MainScreen

db_name = "employees_dummy"    
paymentcall_threshold = 10      # When the pay message got displayed (critical is 1.5 that value)
quantcosts = 0.25               # cost of one quant (can also be 0)
quantname = "Coffee"            # name of your quants

# path gerneration for the DB
subfoldername = "data"
dirpath = os.path.dirname(__file__)
db_path = os.path.join(dirpath, subfoldername, "{}.db".format(db_name))

if __name__ == "__main__":
    # creates the application
    app = QApplication(sys.argv)
    #creates the mainscreen, sets it to fixed size and fullscreen
    w = MainScreen(db_path=db_path, quantname=quantname, quantcosts=quantcosts)
    w.show()
    # runs the app until the exit
    sys.exit(app.exec_())