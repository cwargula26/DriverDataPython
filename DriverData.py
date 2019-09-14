import sys
from fileParser import FileParser
from report import Report
from errorLog import ErrorLog

errorLog = ErrorLog()
errorLog.setPath("error.log")

# Check for an argument that should be a file name
if len(sys.argv) == 1:
    errorLog.log('Please provide the path to an input file')
    print('Please provide the path to an input file')
else:
    parser = FileParser(sys.argv[1])
    data = parser.parse()

    report = Report(data)
    # check if a file is provided for the output report
    if len(sys.argv) > 2:
        report.printReport(sys.argv[2])
    # output the record to the screen
    else:
        report.printReport()