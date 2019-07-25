import os
from fetchData import smartSheet


def initGlobals():
    global MAIN_DIR
    MAIN_DIR = os.getcwd()


if __name__ == "__main__":
    initGlobals()

smartSheet.downloadSmartsheet()
