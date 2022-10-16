import serial
import time


def listener():
    port = input("What is the number of the COM port of your serial cable? ")
    try:
        serialPort  =  serial.Serial(port = F"COM{port}", baudrate=9600, timeout=0.05)
        while True:
            if serialPort.in_waiting > 0:
                x = serialPort.read()
                print(x.decode(), end='')

    except:
        print("Unable to connect to device, Please try again later")


