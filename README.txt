DriverData 9/14/2019

Usage Notes
--------------------
The purpose of the DriverData system is to process a collection of driving history for people.
It then generates a report containing each driver with total miles driven and average speed. 
In the report drivers are ordered by the most miles driven.

Expectations
--------------------
    Example input:
    --------------------
    Driver Dan
    Driver Alex
    Driver Bob
    Trip Dan 07:15 07:45 17.3
    Trip Dan 06:12 06:32 21.8
    Trip Alex 12:01 13:16 42.0

    Input Data Mapping
    --------------------
    (Driver) {DriverName}
    (Trip) {DriverName} {StartTime} {EndTime} {Distance}

    Expected output:
    --------------------
    Alex: 42 miles @ 34 mph
    Dan: 39 miles @ 47 mph
    Bob: 0 miles

    Output Data Mapping
    --------------------
    {DriverName}: {Distance} miles @ {Average Speed} mph

    Business Rules
    --------------------
    Discard any trips that average a speed of less than 5 mph or greater than 100 mph.
    Round miles and miles per hour to the nearest integer.
    Sort the output by most miles driven to least.

Why
--------------------
The purpose of this system is to process information about how a driver drives to base business decisions off of

How to use
--------------------
To run this system use the following command py main.py {full path to input file}

Objects:
--------------------
    FileParser - parses the input file into commands

    DrvierDataCollector - collects all of the commands from the file parser an processes the commands in order 

    Driver - Represents a driver
        Name
        Trips

    Trip - Reprsents a trip
        Start
        End
        Distance
        Average Speed Round((End - Start)/Distance)

Edge Cases
--------------------
1. End date is less than start date
2. Distance is 0 or less than 0
3. Trips for drivers that don't exist
4. Dup drivers
5. Missing Driver data
6. Missing Trip data
7. Unexpected driver data
8. Unexpected trip data
9. Driver without trip data
10. Driver with a trip less than 5 mph
11. Driver with a trip greather than 100 mph

Additional Data
--------------------
Number of trips per driver
Average distance per trip


Alternate Approach (separate files)
--------------------
Find an alternate approach in the folder name AlternateApproach