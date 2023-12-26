import serial
import time

COM_PORT = '/dev/ttyUSB0'
COM_BAUD = 115200
COM_TIMEOUT = 1

serialPort = serial.Serial(
    port=COM_PORT, baudrate=COM_BAUD, timeout=COM_TIMEOUT
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
        except:
            pass
