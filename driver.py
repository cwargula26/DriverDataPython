import sys
from trip import Trip
from errorLog import ErrorLog

class Driver:
    __errorLog = ErrorLog()

    def __init__(self, name):
        self.name = name.replace(' ', '')
        if self.name == '':
            raise Exception('Driver name cannot be an empty string')
        self.trips = []
        self.milesDriven = 0
        self.timeDriven = 0

    # Adds a trip to the current driver
    def addTrip(self, startTime, endTime, distance):
        try:
            trip = Trip(startTime, endTime, float(distance))
            self.trips.append(trip)
            self.milesDriven = self.milesDriven + trip.distance
            self.timeDriven += trip.duration
        except Exception as ex:
            self.__errorLog.log(str(ex))

    # Calculates the average speed that the driver took during all of their trips    
    def averageSpeed(self):
        if self.milesDriven == 0 or self.timeDriven == 0:
            return 0
        else:
            return self.milesDriven/self.timeDriven
