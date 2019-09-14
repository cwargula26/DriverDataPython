import sys
from driverDataCollector import DriverDataCollector
from errorLog import ErrorLog

class FileParser:
    __errorLog = ErrorLog()
    def __init__(self, fileName):
        self.fileName = fileName
        self.driverDataCollector = DriverDataCollector()
    
    # Check the file for data and parse the commands
    def parse(self):
        # Try opening the file provided as the argument
        with open(self.fileName) as inputFile:
            # iterate through each line the file
            for line in inputFile:
                # check for empty lines
                # TODO: make trim a function for strings
                if len(line.replace(" ", "")) > 0:                    
                    # ASSUMPTION: The lines in the file do not matter, so I'm separating the driver commands
                    # from the trip commands so that I can process the drivers first then trips.
                    # Another approach could be to just log trips that don't have drivers yet as errors

                    if line.lower().startswith('driver'):
                        self.driverDataCollector.addDriverCommand(line)
                    elif line.lower().startswith('trip'):
                        self.driverDataCollector.addTripCommand(line)
                    else:
                        self.__errorLog.log("Invalid Command: " + line)
            inputFile.close()
        return self.driverDataCollector.processCommands()
