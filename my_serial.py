import serial
from tkinter import *


root = Tk()
T = Text(root, height=20, width=80)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")


ser = serial.Serial(
    port='/dev/cu.usbmodem1412201',
    baudrate=115200
)

def readSerial():
    response = ser.readline()
    print(response)
    T.insert(END, response)
    T.see(END)
    root.after(50, readSerial) # after 50 milli seconds this is called again

readSerial()

root.mainloop()


