#!/usr/bin/python3.9
# https://buildmedia.readthedocs.org/media/pdf/pyserial/latest/pyserial.pdf

import serial
import time

COM_PORT = '/dev/ttyUSB0'
COM_BAUD = 115200
COM_TIMEOUT = 1

OPCODE_RESET = bytes([7])
OPCODE_START = bytes([128])
OPCODE_SAFE = bytes([131])
OPCODE_FULL = bytes([132])
OPCODE_POWER_DOWN = bytes([133])
OPCODE_CLEAN = bytes([135])
OPCODE_SEEK_DOCK = bytes([143])
OPCODE_OFF = bytes([173])

print(f"Connecting to Serial/USB port: {COM_PORT}")
serialPort = serial.Serial(port=COM_PORT, baudrate=COM_BAUD, timeout=COM_TIMEOUT)
serialString = ""  # Used to hold data coming over UART

while serialPort.in_waiting > 1:
  # Wait until there is data waiting in the serial buffer
  # Read data out of the buffer until a carraige return / new line is found
  print('Printing Initial Roomba output')
  serialString = serialPort.readline()
  # Print the contents of the serial data
  try:
    print(serialString.decode("Ascii"))
  except:
    pass

# Set to START/PASSIVE. (Expect one beep)
print(f"Sending START/PASSIVE signal")
serialPort.write(bytes([128]))
time.sleep(2)
print(f"Sending FULL OPCODE signal")
serialPort.write(bytes([132]))
time.sleep(2)

#print(f"Seeking Dock...")
#serialPort.write(bytes([143]))
print(f"Cleaning...")
serialPort.write(bytes([135]))
time.sleep(12)
#serialPort.write(bytearray([137, 255, 56, 1, 244]))
#time.sleep(30)


print('Sleeping Roomba')
serialPort.write(bytes([128]))
time.sleep(1)
#serialPort.write(bytes([173]))
#serialPort = None

serialPort.close()
