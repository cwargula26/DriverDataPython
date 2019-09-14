import sys
from driver import Driver
from trip import Trip

class Report:
    def __init__(self, driverData):
        self.driverData = driverData

    # Convert Driver data into a readable report
    # This gives the user choices to print to a file or directly to the output
    def printReport(self, fileName=None):
        if self.driverData == None or len(self.driverData) == 0:
            raise Exception("There is no driver data to report")

        lines = []

        # generate data
        # sort users by the most miles driven
        for driver in sorted(self.driverData, key=lambda driver: driver.milesDriven, reverse=True):
            # Rounding the distance and speed sounds like display logic so I moved it here
            # instead of on the driver object which I'm treating as a business object this way
            # if some other consumer wanted exact numbers they're still available
            lines.append("{0} {1} miles @ {2} mph".format(driver.name, str(round(driver.milesDriven)), str(round(driver.averageSpeed()))))

        if fileName == None:
            # output to screen
            print(*lines, sep="\n")
        else:
            # write to specified file
            filePointer = open(fileName, "w")
            data = "\n".join(lines)
            filePointer.write(data)
            filePointer.close()