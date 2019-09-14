import sys
from datetime import datetime, date
from driver import Driver
from trip import Trip
from errorLog import ErrorLog

class DriverDataCollector:
    driverCommands = []
    tripCommands = []
    errors = []
    __errorLog = ErrorLog()

    # Adds a 'Driver' command to an array
    # This is done to separate all of the commands so that the
    # 'Driver' commands can be processed first
    def addDriverCommand(self, command):
        if len(command) > 0:
            commandParts = command.split()
            if len(commandParts) == 2:
                if commandParts[0].lower() == 'driver':
                    # Check for duplicate drivers
                    for driverCommand in self.driverCommands:
                        if driverCommand[1] == commandParts[1]:
                            self.errors.append("Duplicate Command: " + command)
                            return
                    self.driverCommands.append(commandParts)
                    return
        self.errors.append("Invalid Command: " + command)
            
    # Adds a 'Trip' command to an array
    # This is done to separate all of the commands so that the
    # 'Driver' commands can be processed first
    def addTripCommand(self, command):
        if len(command) > 0:
            commandParts = command.split()
            if len(commandParts) == 5:
                if commandParts[0].lower() == 'trip':
                    # Check for duplicate trips
                    for tripCommand in self.tripCommands:
                        if tripCommand[1].lower() == commandParts[1].lower() and tripCommand[2] == commandParts[2] and tripCommand[3] == commandParts[3] and tripCommand[4] == tripCommand[4]:
                            self.errors.append("Duplicate Command: " + command)
                            return
                    self.tripCommands.append(commandParts)
                    return
        self.errors.append("Invalid Command: " + command)

    # Processes all of the commands in order
    def processCommands(self):
        driverData = []
        # process driver commands first to make sure all drivers are added
        for driverCommand in self.driverCommands:
            try:
                driver = None
                driver = Driver(driverCommand[1])

                for tripCommand in self.tripCommands:
                    if tripCommand[1].lower() == driverCommand[1].lower():
                        startTime = datetime.combine(date.today(), datetime.strptime(tripCommand[2], "%H:%M").time())
                        endTime = datetime.combine(date.today(), datetime.strptime(tripCommand[3], "%H:%M").time())
                        driver.addTrip(startTime, endTime, tripCommand[4])
                driverData.append(driver)
            except Exception as ex:
                self.__errorLog.log(str(ex))
        return driverData


    
