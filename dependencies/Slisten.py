import serial

def listener():
    port = input("What is the number of the COM port of your serial cable? ")
    serialPort  =  serial.Serial(port = F"COM{port}", baudrate=9600, timeout=0.05)
    serialString = ""                           # Used to hold data coming over UART
    while(1):
        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):
            # Readdata out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()
            # Print the contents of the serial data
            print(serialString.decode('Ascii'))

