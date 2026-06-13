#!/usr/bin/python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

import curses
import time

import pycreate2

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

if __name__ == "__main__":
    # Create a Create2 bots settings
    port = '/dev/ttyUSB0'
    baud = { 'default': 115200 }

    # Create a Create 2
    bot = pycreate2.Create2(port=port, baud=baud['default'])
    # Start the Create 2
    bot.start()
    # Put the Create2 into 'safe' mode so we can drive it
    # This will still provide soem protection
    bot.safe()
    # You are responsible for handling issues, no protection/safety in
    # this mode ... be careful
    bot.full()
    sensor = bot.get_sensors()
    print(f"{sensor.light_bumper_left:4}")
    print(f"Wall = {sensor.wall:1}")
    print("Foo")

    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                sensors = bot.get_sensors()
                print(sensors)
                break
            elif char == curses.KEY_UP:
                screen.addstr(0, 0, 'up ')
                bot.drive_direct(50,50)
                time.sleep(2.0)
                bot.drive_stop()
            #elif char == curses.KEY_UP:
            #    screen.addstr(0, 0, 'up ')
            #    bot.drive_direct(50,50)
            #    time.sleep(2.0)
            #    bot.drive_stop()
            elif char == curses.KEY_RIGHT:
                screen.addstr(0, 0, 'right ')
                bot.drive_direct(-25,25)
                time.sleep(2.0)
                bot.drive_stop()
            elif char == curses.KEY_DOWN:
                screen.addstr(0, 0, 'down ')
                bot.drive_direct(-50,-50)
                time.sleep(2.0)
                bot.drive_stop()
            elif char == curses.KEY_LEFT:
                screen.addstr(0, 0, 'left ')
                bot.drive_direct(25,-25)
                time.sleep(2.0)
                bot.drive_stop()
    finally:
        # Shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(2)
        bot.stop()
    
    sensors = bot.get_sensors()
    print(sensors)
    print('Bot drive stop')
    bot.drive_stop()
    time.sleep(0.1)
    print('Bot close')
    #bot.close()

