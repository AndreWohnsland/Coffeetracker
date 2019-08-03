import sys
import os

from src.loggerconfig import basiclogger
from ui_elements.setupui import create_main_window
from data.generate_db import create_new_db

devenvironment = True           # enables or disables your cursor
app_width = 480
app_height = 320
db_name = "tracker_test"    
paymentcall_threshold = 10      # When the pay message got displayed (critical is 1.5 that value)
quantcosts = 0.25               # cost of one quant (can also be 0)
quantname = "coffee"            # name of your quants

# path gerneration for the DB
subfoldername = "data"
dirpath = os.path.dirname(__file__)
db_path = os.path.join(dirpath, subfoldername, "{}.db".format(db_name))
print(db_path)

if __name__ == "__main__":
    # create_new_db(db_path)
    basiclogger('debuglog', 'debuglog')
    create_main_window(
        devenvironment,
        db_path,
        app_width=app_width,
        app_height=app_height,
        paymentcall_threshold=paymentcall_threshold,
        quantcosts=quantcosts,
        quantname=quantname
        )
