import unittest
from report import Report

class ReportTests(unittest.TestCase):

    def test_print_report_with_file(self):
        # Without using DI this test would actually write to the filesystem which 
        # makes it a fragile test because the file could already exist
        self.skipTest("Need to implement DI")

    def test_print_report_without_file(self):
        # Without using DI this test would actually write to the filesystem which 
        # makes it a fragile test because the file could already exist
        self.skipTest("Need to implement DI")
    
    def test_without_driver_data(self):
        # Arrange
        report = Report([])

        # Act
        try:
            report.printReport()
            self.assertEqual(1,2)
        except Exception as ex:
            # Asses
            self.assertEqual(str(ex), "There is no driver data to report")