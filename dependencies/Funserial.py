import time
import serial

def send(data, port, baudrate, timeout):
    if baudrate == 0:
        baudrate = 9600
    ser = serial.Serial(port, baudrate, timeout=timeout)
    ser.write(data.encode())
    time.sleep(1)
    ser.close()

