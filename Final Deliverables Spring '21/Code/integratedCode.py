import math
import time
import array
from gpiozero import LED
from tkinter import Tk, Canvas, Frame, BOTH
import numpy as np

### Program Name: RF Direction of Arrival Signal Triangulation
### Created By: Ryan Clayton
### Updated By: Robert Kramer & Krishna Patel
### Date Updated: 04/19/2021
### This program is specifically designed to switch between 8 RF antenna values,
### calculate the direction in degrees of the incoming signal and display the direction.

#declare the switches to GPIO pins
switch1_1 = LED(17); #pin 11
switch1_2 = LED(27); #pin 13
switch1_3 = LED(22); #pin 15
switch2_1 = LED(23); #pin 16
switch2_2 = LED(24); #pin 18
switch2_3 = LED(25); #pin 22
switch3_1 = LED(5); #pin 29
switch3_2 = LED(6); #pin 31


####Antenna switching functions##########################################
def turnSwitch1off():
    #turn switches 1 off
    switch1_3.on();
    switch1_2.on();
    switch1_1.off();

def turnSwitch2off():
    switch2_3.on();
    switch2_2.on();
    switch2_1.off();

def inputFromSwitch1():
    #take input from switch 1 into switch 3
    switch3_1.on();
    switch3_2.off();
    
def inputFromSwitch2():
    #take input from switch 2 into switch 3
    switch3_1.off();
    switch3_2.on();
    
def turnRF1_1on():
    #turn RF1 on
    switch1_1.on();
    sleep(1);
    turnSwitch1off();
    
def turnRF1_2on():
    #turn RF2 on
    switch1_2.on();
    sleep(1);
    turnSwitch1off();
    
def turnRF1_3on():
    #turn RF3 on
    switch1_2.on();
    switch1_1.on();
    sleep(1);
    turnSwitch1off();

def turnRF1_4on():
    #turn RF4 on
    switch1_3.on();
    sleep(1);
    turnSwitch1off();

def turnRF2_1on():
    #turn RF1 on
    switch2_1.on();
    sleep(1);
    turnSwitch2off();

def turnRF2_2on():
    #turn RF2 on
    switch2_2.on();
    sleep(1);
    turnSwitch2off();

def turnRF2_3on():
    #turn RF3 on
    switch2_1.on();
    switch2_2.on();
    sleep(1);
    turnSwitch2off();
    
def turnRF2_4on():
    #turn RF4 on
    switch2_3.on();
    sleep(1);
    turnSwitch2off();

#####Calculations#############################################

def getDirectionOfArrivalVector(antValue):
    directionVector = [0, 0]
    for i in range(8):
        directionVector[0] = directionVector[0] + (antValue[i] * (math.cos(math.radians(i * 45))))
        directionVector[1] = directionVector[1] + (antValue[i] * (math.sin(math.radians(i * 45))))
    print(" Angle Of Arrival Vector = [{:2.2f}, {:2.2f}]".format(directionVector[0], directionVector[0]))
    return directionVector

def getDirectionOfArrival(directionVector):
    doa = math.degrees(math.atan(directionVector[1] / directionVector[0]))
    if (directionVector[0] < 0):
        doa = doa + 180
    if (doa >= 360):
        doa = doa - 360
    if (doa < 0):
        doa = doa + 360
    return doa

def runAntennaCalc(antennaAverages):
    directionOfArrivalVector = getDirectionOfArrivalVector(antennaAverages)
    directionOfArrival = getDirectionOfArrival(directionOfArrivalVector)
    print("        Angle of Arrival = {:.2f} Degrees".format(directionOfArrival))

####Direction GUI###################################################

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Direction Calculator")
        self.pack(fill=BOTH, expand=1)

        angle = 91
        x = 900
        y = 900
        rB = 0.35 * y
        rL = 0.02 * y
        cxB = x * 0.5
        cyB = y * 0.5
        cxL = cxB + (rB * (math.cos(math.radians(angle))))
        cyL = cyB + (rB * (math.sin(math.radians(angle))))

        canvas = Canvas(self)
        canvas.configure(bg='black')
        canvas.create_oval(cxB - rB, cyB - rB, cxB + rB, cyB + rB, outline="#cc0000", fill="#ffffff", width=y * .01)
        canvas.create_oval(cxL - rL, cyL - rL, cxL + rL, cyL + rL, outline="#cc0000", fill="#ffffff", width=y * .005)
        angleString = ("{} Degrees".format(angle))
        canvas.create_text(cxB, cyB, fill="#000000", font=200, text=angleString)
        canvas.pack(fill=BOTH, expand=1)
    
####Main################################################################# 
def main():
   turnSwitch1off();
    turnSwitch2off();
    i = 0;
    while True:
        inputFromSwitch1();
        turnRF1_1on();
#sample data using GNU Radio
     ##sleep for short time

#convert the data (Krishna's code)
# Read complex binary
# open filename and return the contents as a column vector treating
# them as 32 bit complex numbers
filename = r"C:\Users\patel\PycharmProjects\read_complex_binary\print_test2.dat" #don't know what the file name will be until ran
content = np.fromfile(open(filename), dtype=np.float32)
for x in content:
    a_file = open("ConvertedData.txt", "w+")
    print(content, a_file)
    np.savetxt(a_file, content)
#print to a array
     ###create arrays (8 of them, 1 for each antenna)
        antenna1_array = array.array('f', []);
        antenna2_array = array.array('f', []);
        antenna3_array = array.array('f', []);
        antenna4_array = array.array('f', []);
        antenna5_array = array.array('f', []);
        antenna6_array = array.array('f', []);
        antenna7_array = array.array('f', []);
        antenna8_array = array.array('f', []);
     ###open file
        data_file = open("ConvertedData.txt", "r");
         #read line by line
        f1 = data_file.readlines()
         #put each line in file into separate array slot
        for x in f1:
            antenna1_array.append(x)
#print array contents to see if it worked
        for x in antenna1_array:
            print(x)
#average the arrays
        for x in antenna1_array:
            y = y + x
        average1 = y / len(antenna1_array);
        y = 0;
        for x in antenna2_array:
            y = y + x
        average2 = y / len(antenna2_array);
        y = 0;
        for x in antenna3_array:
            y = y + x
        average3 = y / len(antenna3_array);
        y = 0;
        for x in antenna4_array:
            y = y + x
        average4 = y / len(antenna4_array);
        y = 0;
        for x in antenna5_array:
            y = y + x
        average5 = y / len(antenna5_array);
        y = 0;
        for x in antenna6_array:
            y = y + x
        average6 = y / len(antenna6_array);
        y = 0;
        for x in antenna7_array:
            y = y + x
        average7 = y / len(antenna7_array);
        y = 0;
        for x in antenna8_array:
            y = y + x
        average8 = y / len(antenna8_array);
        time.sleep(1);
        i = i + 1;
        turnRF1_2on();
        time.sleep(1);
        i = i + 1;
        turnRF1_3on();
        time.sleep(1);
        i = i + 1;
        turnRF1_4on();
        time.sleep(1);
        i = i + 1;
        inputFromSwitch2();
        turnRF2_1on();
        time.sleep(1);
        i = i + 1;
        turnRF2_2on();
        time.sleep(1);
        i = i + 1;
        turnRF2_3on();
        time.sleep(1);
        i = i + 1;
        turnRF2_4on();
        time.sleep(1);
        turnSwitch1Off();
        turnSwitch2Off();
    #do calculations for all 8 arrays
        antennaAverage = array.array('f', [average1, average2, average3, average4, average5, average6, average7, average8]);
        runAntennaCalc(antennaAverage);

        print ("%d", i);
        i = 0;
        root = Tk()
        ex = Example()
        root.geometry("900x900+300+300")
        root.mainloop()

if __name__ == '__main__':
    main()
