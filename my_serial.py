import serial
from tkinter import *
import serial.tools.list_ports


import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('800x600')

labelTop = tk.Label(app,
                    text = "Serials")
labelTop.grid(column=0, row=0)

my_serials = []
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    my_serials.append(port)

comboExample = ttk.Combobox(app, 
                            values=my_serials)
comboExample.grid(column=0, row=1)
comboExample.current(1)

print(comboExample.get())

T = Text(app, height=20, width=80)
T.pack()
T.insert(END, "Output")
T.grid(column=0, row=2)

ser = serial.Serial(
    port='/dev/cu.usbmodem1412201',
    baudrate=115200
)

def readSerial():
    response = ser.readline()
    T.insert(END, response)
    T.see(END)
    app.after(50, readSerial) # after 50 milli seconds this is called again

readSerial()

T = Text(app, height=20, width=5        )
T.pack()
T.insert(END, "Output")
T.grid(column=0, row=2)

app.mainloop()



