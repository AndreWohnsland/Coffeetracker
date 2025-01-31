import sys
import os

from PyQt5.QtWidgets import QApplication

from data.generate_db import create_new_db
from desctop_ui.desctopapp_src import MainScreen, get_properties, standartbox


# path gerneration for the DB, and the configs
dirpath = os.path.dirname(__file__)
db_path, paymentcall_threshold, quantcosts, quantname, occured_error = get_properties(dirpath)

if __name__ == "__main__":
    go_on = True
    app = QApplication(sys.argv)
    # creates the application, in case of an error tries to handle it, if its resolved go on else dont open the main dialog
    if occured_error:
        go_on = False
        # searching for the db. logig needs to be implemented here:
        user_return = standartbox(
            "An Error connecting to the DB occured. Please check that the Pi is in the same Network and the programm was installed correctly! Want to switch to local mode? Else closing ...",
            boxtype="okcancel", okstring='local', cancelstring='quit')
        # switching to local mode instead.
        if user_return == 1024:
            db_path, paymentcall_threshold, quantcosts, quantname, occured_error = get_properties(dirpath, path_not_found=True)
            go_on = True
    if go_on:
        #creates the mainscreen, sets it to fixed size and fullscreen
        create_new_db(db_path)
        w = MainScreen(db_path=db_path, quantname=quantname, quantcosts=quantcosts, dirpath=dirpath)
        w.show()
        # runs the app until the exit
        sys.exit(app.exec_())
        w.DB.close()
