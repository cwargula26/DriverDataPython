from datetime import datetime, date, time, timedelta

class Trip:
    def __init__(self, startTime, endTime, distance):
        if distance < 0:
            raise Exception('Distance must be a positive number')
        if endTime <= startTime:
            raise Exception('End Time must be after Start Time')
        self.startTime = startTime
        self.endTime = endTime
        self.distance = distance
        self.mph = self.calculateMph()
        if self.mph < 5:
            raise Exception('Skip trip: Less than 5mph')
        elif self.mph > 100:
            raise Exception('Skip trip: Greater than 100mph')

    def calculateMph(self):
        # Subtract start time from end time
        durationInSeconds = (self.endTime.timestamp() - self.startTime.timestamp())
        # Divde seconds by 3600 to get hrs in decimal
        self.duration = durationInSeconds/3600
        # Divide distance by time 
        mph = self.distance/self.duration
        # Round result
        return mph.__round__()

