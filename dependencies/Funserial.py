import time
import serial
import sys

def send(data, port, baudrate, timeout):
    if baudrate == 0:
        baudrate = 9600
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        ser.write(data.encode())
        time.sleep(1)
        ser.close()
    except:
        print("Unable to send configuration to device, Please manually configure")

