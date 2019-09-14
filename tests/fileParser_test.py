import unittest
import sys
import os
from fileParser import FileParser

class FileParserTests(unittest.TestCase):
    testFilePath = "test_input.txt"
    validData = "Driver Chris"
    invalidData = "hello world"

    def create_file(self, data):
        # Write test file for input
        with open(self.testFilePath, "w") as testFile:
            testFile.write(data)
            testFile.close()

    def test_valid_file(self):
        # Arrange
        self.create_file(self.validData)

        # Act
        filePaser = FileParser(self.testFilePath)
        try:
            filePaser.parse()
            self.assertEqual(1, 1)
        except Exception:
            self.assertEqual(1,2)

        # Clean up
        os.remove(self.testFilePath)
    
    def test_invalid_file(self):
        # Arrange

        # Act
        fileParser = FileParser('invalidFileName.blah')
        try:
            fileParser.parse()
            self.assertEqual(1,2)
        except Exception:
            # Assert
            self.assertTrue

    def test_valid_data(self):
        # TODO: research dependency injection in python for this test
        self.skipTest("Need DI to make this a valid test")
        # # Arrange
        # self.create_file(self.validData)

        # # Act
        # filePaser = FileParser(self.testFilePath)
        # try:
        #     data = filePaser.parse()
        #     self.assertEqual(len(data), 1)
        # except Exception:
        #     self.assertEqual(1,2)

    def test_invalid_data(self):
        # TODO: research dependency injection in python for this test
        self.skipTest("Need DI to make this a valid test")
        # self.assertEqual(1,2)
