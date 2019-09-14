import sys
from datetime import datetime

class ErrorLog():
    __instance = None
    __errorFilePath = ""

    def __new__(self):
        if ErrorLog.__instance is None:
            ErrorLog.__instance = object.__new__(self)
        return ErrorLog.__instance

    # Sets the path of the error log file
    def setPath(self, filePath):
        self.__instance.__errorFilePath = filePath
    
    # Writes an error message to the log
    def log(self, errorMessage):
        errorFile = open(self.__instance.__errorFilePath, "a")
        errorFile.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + errorMessage + "\n")
        errorFile.close()