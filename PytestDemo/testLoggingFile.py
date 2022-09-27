import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler("logfile.log")



    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s :%(message)s")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object file location simple
    logger.setLevel(logging.DEBUG) ## skip debug information

    logger.debug("a debug statement is executed")
    logger.info("information statements")
    logger.warning("something is in warning mode")
    logger.error("a major error has happened")
    logger.critical("Critical issue")

