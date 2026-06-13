#!/usr/bin/env python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

import curses
import logging
import time

import pycreate2

logfile='/home/emanners/Code/Robotics/iRobotCreate2/sensor.log'
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('============== Logs ==============')

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
    # This will still provide some protection
    bot.safe()
    time.sleep(0.5)
    # You are responsible for handling issues, no protection/safety in
    # this mode ... be careful
    bot.full()

    try:
        sensors = bot.get_sensors()
    except Exception as e:
        print(f"Error: {e}")
        logging.info('Exception: %s', e)
        logging.info('Exception: Be sure to cleanly stop bot')
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(2)
        bot.stop()
        time.sleep(2.0)
        exit()
    else:
        logging.info('Else: No Exceptions moving on.')
    finally:
        logging.info('Finally')
    
    # Grab sensor data
    sensors.wall == sensors[1]
    sensors.charger_state == sensors[13]
    sensors.charger_available == sensors[24]
    # Print sensor data
    screen.addstr(20, 0, str(sensors.wall))
    screen.addstr(21, 0, str(sensors.charger_state))
    screen.addstr(22, 0, str(sensors.charger_available))

    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                screen.addstr(30, 0, '**Quitting...**')
                time.sleep(1.0)
                break
            elif char == curses.KEY_UP:
                screen.addstr(0, 0, 'up ')
                bot.drive_direct(50,50)
                time.sleep(2.0)
                bot.drive_stop()
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
    
    print('Bot drive stop')
    bot.drive_stop()
    time.sleep(0.1)
    print('Bot close')
    #bot.close()

