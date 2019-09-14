import unittest
from driverDataCollector import DriverDataCollector

class DriverDataCollectorTests(unittest.TestCase):
    validDriverCommand = "Driver Dan"
    invalidDriverCommand = "Driver"
    validTripCommand = "Trip Dan 07:15 07:45 17.3"
    invalidTripCommand = "Trip"

    def test_add_valid_driver(self):
        # Arrange
        # TODO: for some reason it appears that each test is using the same memory address
        # which causes subsequent tests to fail
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addDriverCommand(self.validDriverCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.driverCommands), 1)
        self.assertEqual(len(driverDataCollector.errors), 0)

        # Cleanup
        del driverDataCollector

    def test_add_invalid_driver(self):
        # Arrange
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addDriverCommand(self.invalidDriverCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.driverCommands), 0)
        self.assertEqual(len(driverDataCollector.errors), 1)

        # Cleanup
        del driverDataCollector

    def test_add_duplicate_driver(self):
        # Arrange
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addDriverCommand(self.validDriverCommand) 
        driverDataCollector.addDriverCommand(self.validDriverCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.driverCommands), 1)
        self.assertEqual(len(driverDataCollector.errors), 1)

        # Cleanup
        del driverDataCollector

    def test_add_valid_trip(self):
        # Arrange
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addTripCommand(self.validTripCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.tripCommands), 1)
        self.assertEqual(len(driverDataCollector.errors), 0)

        # Cleanup
        del driverDataCollector

    def test_add_invalid_trip(self):
        # Arrange
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addTripCommand(self.invalidTripCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.tripCommands), 0)
        self.assertEqual(len(driverDataCollector.errors), 1)

        # Cleanup
        del driverDataCollector

    def test_add_duplicate_trip(self):
        # Arrange
        driverDataCollector = DriverDataCollector()
        driverDataCollector.driverCommands = []
        driverDataCollector.errors = []
        driverDataCollector.tripCommands = []

        # Act
        driverDataCollector.addTripCommand(self.validTripCommand) 
        driverDataCollector.addTripCommand(self.validTripCommand) 

        # Assert
        self.assertEqual(len(driverDataCollector.tripCommands), 1)
        self.assertEqual(len(driverDataCollector.errors), 1)

        # Cleanup
        del driverDataCollector
