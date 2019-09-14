import unittest
import sys
from datetime import datetime, date, time
from trip import Trip

class TripTests(unittest.TestCase):
    # To make the math easy just leave the start and end times to be an hour a part
    validStartTime = datetime.combine(date.today(), datetime.strptime("00:00", "%H:%M").time())
    validEndTime = datetime.combine(date.today(), datetime.strptime("01:00", "%H:%M").time())
    validDistance = 30
    invalidDurationFiveMph = 4
    invalidDurationOneHundredMph = 101
    invalidDistance = -10

    def test_valid_trip(self):
        try:
            trip = Trip(self.validStartTime, self.validEndTime, self.validDistance)
            self.assertEqual(trip.distance, self.validDistance)
        except Exception as ex:
            self.assertEqual(1,2)

    def test_invalid_trip_end_before_start(self):
        try:
            trip = Trip(self.validEndTime, self.validStartTime, self.validDistance)
            self.assertEqual(1,2)
        except Exception as ex:
            self.assertEqual(str(ex), 'End Time must be after Start Time')

    def test_invalid_trip_negative_distance(self):
        try:
            trip = Trip(self.validStartTime, self.validEndTime, self.invalidDistance)
            self.assertEqual(1,2)
        except Exception as ex:
            self.assertEqual(str(ex), 'Distance must be a positive number')

    def test_invalid_trip_lt_five_mph(self):
        try:
            trip = Trip(self.validStartTime, self.validEndTime, self.invalidDurationFiveMph)
            self.assertEqual(1,2)
        except Exception as ex:
            self.assertEqual(str(ex), 'Skip trip: Less than 5mph')

    def test_invalid_trip_gt_one_hundred_mph(self):
        try:
            trip = Trip(self.validStartTime, self.validEndTime, self.invalidDurationOneHundredMph)
            self.assertEqual(1,2)
        except Exception as ex:
            self.assertEqual(str(ex), 'Skip trip: Greater than 100mph')
