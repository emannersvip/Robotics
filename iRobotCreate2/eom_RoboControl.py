#!/usr/bin/python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

# https://raspberry-valley.azurewebsites.net/Map-Bluetooth-Controller-using-Python/
from evdev import InputDevice, categorize, ecodes

import curses
import time

import pycreate2

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
    # See README.txt
    try:
        gamepad = InputDevice('/dev/input/event2')
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
    # Start the Create 2
    bot.start()
    # Put the Create2 into 'safe' mode so we can drive it
    # This will still provide some protection
    bot.safe()
    # You are responsible for handling issues, no protection/safety in
    # this mode ... be careful
    bot.full()

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

