import math
import time

# from directionGUI import main_2


### Program Name: RF Direction of Arrival Signal Triangulation
### Created By: Ryan Clayton
### Date Updated: 02/15/2021
### This program is specifically designed to accept 8 RF antenna values
### and calculate the direction in degrees of the incoming signal.

f = open('printDOA.txt', 'w+')

def main():
    executeTestCases()


def executeTestCases():
    for i in range(1):
        file = "antennaTestCase{}.txt".format(i + 1)
        runTestCase(file, i + 1)
        time.sleep(1);


def getDirectionOfArrivalVector(antValue):
    directionVector = [0, 0]
    for i in range(8):
        directionVector[0] = directionVector[0] + (antValue[i] * (math.cos(math.radians(i * 45))))
        directionVector[1] = directionVector[1] + (antValue[i] * (math.sin(math.radians(i * 45))))
    print(" Angle Of Arrival Vector = [{:2.2f}, {:2.2f}]".format(directionVector[0], directionVector[0]))
    return directionVector


def getDirectionOfArrival(directionVector):
    doa = math.degrees(math.atan(directionVector[1] / directionVector[0]))
    if directionVector[0] < 0:
        doa = doa + 180
    if doa >= 360:
        doa = doa - 360
    if doa < 0:
        doa = doa + 360
    return doa


def printAntennaValues(antValue):
    print("Antenna Gains: ", end="")
    for i in range(len(antValue)):
        print("[{}]{:.2f}".format(i + 1, antValue[i]), end=" ")
    print("\n")


def printResults(antValues):
    printAntValues(antValues)


def readAntennaValues(file):
    f = open(file, "r")
    antValue = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(antValue)):
        antValue[i] = float(f.readline())
    return antValue


def runFileCalc(antennaDataFile):
    antennaValues = readAntennaValues(antennaDataFile)
    printAntennaValues(antennaValues)
    directionOfArrivalVector = getDirectionOfArrivalVector(antennaValues)
    directionOfArrival = getDirectionOfArrival(directionOfArrivalVector)
    print("        Angle of Arrival = {:.2f} Degrees".format(directionOfArrival))
    f.write("{:.2f}".format(directionOfArrival))
    f.close()
    return directionOfArrival



def runTestCase(testCaseFile, testCaseNumber):
    print("\n====================================== TEST CASE #{} ======================================\n".format(
        testCaseNumber))
    runFileCalc(testCaseFile)


if __name__ == '__main__':
    main()
