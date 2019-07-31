import sys
import os

from ui_elements.setupui import create_main_window
from data.generate_db import create_new_db

devenvironment = True
app_width = 480
app_height = 320
db_name = "tracker_test"
paymentcall_treshhold = 10
quantcosts = 0.25
quantname = "coffee"

# path gerneration for the DB
subfoldername = "data"
dirpath = os.path.dirname(__file__)
db_path = os.path.join(dirpath, subfoldername, "{}.db".format(db_name))
print(db_path)

if __name__ == "__main__":
    # create_new_db(db_path)
    create_main_window(
        devenvironment,
        db_path,
        app_width=app_width,
        app_height=app_height,
        paymentcall_treshhold=paymentcall_treshhold,
        quantcosts=quantcosts,
        quantname=quantname
        )
