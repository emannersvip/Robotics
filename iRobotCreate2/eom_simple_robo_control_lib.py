## Authors
 # Manikandan Jeyarajan

## References
 # Create2 Open Interface Spec - http://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf?la=en
 # http://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/Python_Tethered_Driving.pdf 
 # https://petrimaki.com/2013/04/28/reading-arduino-serial-ports-in-windows-7/
 # https://pyserial.readthedocs.io/en/latest/shortintro.html

import serial
import time

# Add code to fetch and set COM port dynamically
#COM_PORT = 'COM4'
COM_PORT = '/dev/ttyUSB0'
START = '128'
SAFE_MODE = '131'
DRIVE = '137'
STOP = '173'
DEFAULT_VELOCITY = 200
ser = serial.Serial(COM_PORT, baudrate=115200, timeout=1)

def getReady():    
    __sendCommand(START)
    __sendCommand(SAFE_MODE)
    
def finish():
    ser = None
    __sendCommand(STOP)
    
def __format_to_two_bytes(val):
	binformat = bin(val & 0b1111111111111111)
	hexformat = hex(int(binformat, 2))
	firstbyte, secondbyte = divmod(int(hexformat,16), 0x100)
	return str(firstbyte) + ' ' + str(secondbyte)

def __sendCommand(command):
    cmd = ""
    for v in command.split():
        print(f"v: {v}")
        print('v-int: {}'.format(int(v)))
        print('v-chr: {}'.format(chr(int(v))))
        cmd += chr(int(v)) 
    # https://stackoverflow.com/questions/35642855/python3-pyserial-typeerror-unicode-strings-are-not-supported-please-encode-to
    print(f"cmd: {cmd}\n")
    #ser.write(cmd.encode())
    ser.write(command.encode())
    time.sleep(1)
	
def driveRobot(velocity, radius):
	command = DRIVE + ' ' + __format_to_two_bytes(velocity) + ' ' + __format_to_two_bytes(radius)
	__sendCommand(command)

def driveForward(velocity):
    driveRobot(velocity, 32768)    

def driveForwardFor(duration):
    driveForward(DEFAULT_VELOCITY)
    time.sleep(duration)
    
def driveBackward(velocity):
	driveRobot(-1 * velocity, 32768)
	
def driveBackwardFor(duration):
    driveBackward(DEFAULT_VELOCITY)
    time.sleep(duration)
    
def rotateClockwise(velocity):
	driveRobot(velocity, -1)

def rotateClockwiseFor(duration):
    rotateClockwise(DEFAULT_VELOCITY)
    time.sleep(duration)
    
def rotateCounterClockwise(velocity):
	driveRobot(velocity, 1)
	
def rotateCounterClockwiseFor(duration):
    rotateCounterClockwise(DEFAULT_VELOCITY)
    time.sleep(duration)
    
def turnRight():
    rotateClockwiseFor(0.2)
    
def turnLeft():
    rotateCounterClockwiseFor(0.6)
    
def turnAround():
    rotateClockwiseFor(1.3)
    
def parkRobot():
	driveRobot(0,0)

def beep():
    __sendCommand('140 3 1 64 16 141 3')

if __name__ == "__main__":
    print(f"Hello World\n")
    getReady()
    beep()
    finish()



 # Yes, Create 2 displays all kinds of internal debugging messages in plain text when it is not in an open interface mode. (For a less obtuse one, try putting it on the dock while you are connected to the serial port!) These will go away once you enter OI mode (op code 128).
