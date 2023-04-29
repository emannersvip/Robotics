#!/usr/bin/python3
# iRobotCreate 2 sensors
# https://pypi.org/project/pycreate2/
# https://github.com/MomsFriendlyRobotCompany/pycreate2/tree/master/docs/Markdown

import curses
# https://docs.python.org/3/howto/logging.html
import logging

import pycreate2

logfile = '/home/emanners/Code/iRobotCreate2/sensor.log'
# Setup logging of iRobot Create2 data
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
# Print timestamp everytime we start the progam
logging.info(' =========== Program BEGIN ====================')

# Setup curses screen
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
    # You are responsible for handling issues, no protection/safety in
    # this mode ... be careful
    bot.full()

    # Initialize and get sensor data
    try:
        sensors = bot.get_sensors()
    finally:
        print('Done')

    sensors.battery_capacity == sensors[18]
    sensors.battery_charge == sensors[17] 
    sensors.charger_state == sensors[13] 
    sensors.charger_available == sensors[24] 
    sensors.temperature == sensors[16] 
    # TODO: Fix this to not log percentage while charging
    # Use charger state variable
    battery_life = sensors.battery_charge / sensors.battery_capacity * 100
    temp_farenheit = ( sensors.temperature * 1.8 ) + 32

    logging.info('Charger State: ' + str(sensors.charger_state))
    logging.info('Charger Available: ' + str(sensors.charger_available))
    logging.info('Battery Capacity: ' + str(sensors.battery_capacity) + 'mAh')
    logging.info('Battery Charge: ' + str(sensors.battery_charge) + 'mAh (' + str(battery_life) + ')%')
    logging.info('Temperature: ' + str(sensors.temperature) + 'C / ' + str(int(temp_farenheit)) + 'F')

    screen.addstr(0, 0, str(sensors.charger_state))
    screen.addstr(1, 0, str(sensors.charger_available))
    screen.addstr(2, 0, str(sensors.battery_charge))
    screen.addstr(3, 0, str(sensors.battery_capacity))
    screen.addstr(4, 0, str(sensors.temperature))

    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
    finally:
        # Shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        bot.stop()
        logging.info(' ========== Program END ======================')
    
