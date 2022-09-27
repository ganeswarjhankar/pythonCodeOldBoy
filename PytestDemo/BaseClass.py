import inspect
import logging
class BaseClass:
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s :%(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object file location simple
        logger.setLevel(logging.DEBUG)  ## skip debug information
        return logger




