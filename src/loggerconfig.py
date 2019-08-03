""" Special configs for the Logger """
import logging
import time
from functools import wraps
import os

supress_error = False


def basiclogger(loggerobj, loggername, printline = False):
    """ This is a very basic logger, which logs every Level and writes the time
    and a Message.

    arguments:

        -- loggerobj (str): Name for the loggerobject to later call on
        -- loggername (str): Name of the loggingfile
        -- printline (bool): Condition if the logger should log a restarting line into the log to see all restarts/crashes
    """
    logger = logging.getLogger(loggerobj)
    logger.setLevel(logging.DEBUG)
    dirpath = os.path.dirname(__file__)
    subfoldername = "logs"
    savepath = os.path.join(dirpath, '..', subfoldername, "{}.log".format(loggername))
    # print(savepath)
    fh = logging.FileHandler(savepath)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(message)s', "%Y-%m-%d %H:%M")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    # Logging the Start of the Programm. If it runs a whole evening, each restart means a previous crash.
    if printline:
        template = "{:-^80}"
        logger.debug(template.format("Restarting the Programm",))


def logerror(func):
    """ Logs every time an error occours """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if supress_error:
            logger = logging.getLogger('debuglog')
            try:
                func(*args, **kwargs)
                # return func(*args, **kwargs)
            except Exception:
                logger.exception
                logger.exception("The function {} could not be fully excecuted!".format(func.__name__))
                print("The function {} could not be fully excecuted!".format(func.__name__))
        else:
            func(*args, **kwargs)
    return wrapper
