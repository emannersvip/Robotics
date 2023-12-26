#!/usr/bin/python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

# https://raspberry-valley.azurewebsites.net/Map-Bluetooth-Controller-using-Python/
from evdev import InputDevice, categorize, ecodes

import curses
import time

try:
    import pycreate2
except ImportError:
    print('Import error', 'Please install pyreate2.')
    raise
try:
    import serial
except ImportError:
    print('Import error', 'Please install pyserial.')
    raise

# Button mappings
aBtn = 305
bBtn = 304
xBtn = 307
yBtn = 306
lBmpr = 308
rBmpr = 309
homeBtn = 316

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

if __name__ == "__main__":
    # Create a BT GamePad settings
    # ~---------- See README.txt ----------~ #
    # Make this more helpful and automatic.
    try:
        gamepad = InputDevice('/dev/input/event1')
    except FileNotFoundError as e:
        print(f"Please connect BT")
        time.sleep(2)
        # Shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(2)
        exit()

    # Create a Create2 bots settings
    port = '/dev/ttyUSB0'
    baud = { 'default': 115200 }

    # Create a Create 2
    bot = pycreate2.Create2(port=port, baud=baud['default'])
    ser = serial.Serial(port, baudrate=115200, timeout=1)
    # Start the Create 2
    bot.start()
    # Put the Create2 into 'safe' mode so we can drive it
    # This will still provide some protection
    bot.safe()
    # You are responsible for handling issues, no protection/safety in
    # this mode ... be careful
    bot.full()
    sensors = bot.get_sensors()

    song1 = [59, 64, 62, 32, 69, 96, 67, 64, 62, 32, 60, 96, 59, 64, 59, 32, 59, 32, 60, 32, 62, 32, 64, 96, 62, 96]
    song2 = [76, 16, 76, 16, 76, 32, 76, 16, 76, 16, 76, 32, 76, 16, 79, 16, 72, 16, 74, 16, 76, 32, 77, 16, 77, 16, 77, 16, 77, 32, 77, 16]
    song3 = [76, 12, 76, 12, 20, 12, 76, 12, 20, 12, 72, 12, 76, 12, 20, 12, 79, 12, 20, 36, 67, 12, 20, 36]
    song4 = [72, 12, 20, 24, 67, 12, 20, 24, 64, 24, 69, 16, 71, 16, 69, 16, 68, 24, 70, 24, 68, 24, 67, 12, 65, 12, 67, 48]
    
    #print(">> song len: ", len(song2)//3)

    #song_num = 3
    #bot.createSong(song_num, song3)
    #time.sleep(0.1)
    #how_long = bot.playSong(song_num)

    #print('Sleeping for: ', how_long)
    #time.sleep(how_long)
    #ser.write(173)
    #ser.write('140 3 1 64 16 141 3')
    ser.write(135)

    try:
        #while True:
        #    char = screen.getch()
        #    if char == ord('q'):
        #        break
        #    elif char == curses.KEY_UP:
        #        screen.addstr(0, 0, 'up ')
        #        bot.drive_direct(50,50)
        #        time.sleep(2.0)
        #        bot.drive_stop()
        #    elif char == curses.KEY_RIGHT:
        #        screen.addstr(0, 0, 'right ')
        #        bot.drive_direct(-25,25)
        #        time.sleep(2.0)
        #        bot.drive_stop()
        #    elif char == curses.KEY_DOWN:
        #        screen.addstr(0, 0, 'down ')
        #        bot.drive_direct(-50,-50)
        #        time.sleep(2.0)
        #        bot.drive_stop()
        #    elif char == curses.KEY_LEFT:
        #        screen.addstr(0, 0, 'left ')
        #        bot.drive_direct(25,-25)
        #        time.sleep(2.0)
        #        bot.drive_stop()

        for event in gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == aBtn or event.code == rBmpr:
                        screen.addstr(0, 0, 'Right')
                        bot.drive_direct(-25,25)
                        time.sleep(2.0)
                        bot.drive_stop()
                    elif event.code == bBtn:
                        screen.addstr(0, 0, 'Down ')
                        bot.drive_direct(-50,-50)
                        time.sleep(2.0)
                        bot.drive_stop()
                    elif event.code == xBtn:
                        screen.addstr(0, 0, 'Up   ')
                        bot.drive_direct(50,50)
                        time.sleep(2.0)
                        bot.drive_stop()
                    elif event.code == yBtn or event.code == lBmpr:
                        screen.addstr(0, 0, 'Left ')
                        bot.drive_direct(25,-25)
                        time.sleep(2.0)
                        bot.drive_stop()
                    elif event.code == homeBtn:
                        screen.addstr(0, 0, 'Going Home: ')
                        print(f"HOME")
                        #print(">> song len: ", len(song4)//3)
                        #song_num = 4
                        #bot.createSong(song_num, song4)
                        #time.sleep(0.1)
                        #how_long = bot.playSong(song_num)
                        #print('Sleeping for: ', how_long)
                        #time.sleep(how_long)
                        break
                    else:
                        print(categorize(event))
    finally:
        # Shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(2)
        bot.stop()
    
    print('Bot drive stop')
    bot.drive_stop()
    time.sleep(0.1)
    print('Bot close')
    #bot.close()

