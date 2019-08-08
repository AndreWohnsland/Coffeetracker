import sys
import os

from PyQt5.QtWidgets import QApplication

from desctop_ui.desctopapp_src import MainScreen, get_properties


# path gerneration for the DB, and the configs
dirpath = os.path.dirname(__file__)
db_path, paymentcall_threshold, quantcosts, quantname, occured_error = get_properties(dirpath)

if __name__ == "__main__":
    if not occured_error:
        # creates the application
        app = QApplication(sys.argv)
        #creates the mainscreen, sets it to fixed size and fullscreen
        w = MainScreen(db_path=db_path, quantname=quantname, quantcosts=quantcosts)
        w.show()
        # runs the app until the exit
        sys.exit(app.exec_())
    else:
        pass