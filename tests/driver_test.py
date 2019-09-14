import unittest
from driver import Driver

class DriverTests(unittest.TestCase):
    validDriverName = 'Chris'
    invalidDriverName = ''
    def test_valid_driver(self):
        try:
            driver = Driver(self.validDriverName)
            self.assertEqual(driver.name, self.validDriverName)
        except Exception:
            self.assertEqual(1,2)

    def test_invalid_driver(self):
        try:
            driver = Driver(self.invalidDriverName)
            self.assertEqual(1,2)
        except Exception as ex:
            self.assertEqual(str(ex),'Driver name cannot be an empty string')
