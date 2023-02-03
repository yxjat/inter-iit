import serial
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


arduino_port = "/dev/tty.usbmodem1301" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="analog-data.csv"

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")


samples = 360 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
sensor_data = [] #store data

# collect the samples
while line < samples:
    getData=ser.readline()
    dataString = getData.decode('utf-8')
    data=dataString[0:][:-2]
    #print(data)

    readings = data.split(",")
    #print(readings)
    
    sensor_data.append(readings)
    #print(sensor_data)

    line = line+1

with open(fileName, 'w', encoding='UTF8', newline='') as f:
    dw = csv.DictWriter(f, delimiter=',', fieldnames = ["Degree", "Distance"])
    writer = csv.writer(f)
    dw.writeheader()
    writer.writerows(sensor_data)
#fileName.to_csv(fileName,labels = ["Degree","Distance"])
print("Data collection complete!")
file.close()

f = pd.read_csv(fileName)
deg = f["Degree"]
r = f["Distance"]
for i in range(360):
    plt.polar(deg[i],r[i],"g.")
plt.show()

x,y = pol2cart(r,deg)
