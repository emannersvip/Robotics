#!/usr/bin/env python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

# RaspBerry Pi Package dependencies:
# `sudo apt-get -y install libopenblas-dev libwebpdemux2 libwebpmux3 libopenjp2-7 libswscale-dev libavcodec-dev libavformat-dev libatlas-base-dev`
# `sudo apt install libavformat59 libavcodec-dev libgtk-3-dev`

import argparse
import curses
import cv2
import logging
import numpy as np
import os
import time

import pycreate2

# Setup global and  environment variables
logfile='/home/emanners/Documents/Git/Robotics/Alpha/sensor.log'
os.environ['QT_QPA_PLATFORM']='xcb'
red='\033[31m'
green='\033[32m'
yellow='\033[33m'
blue='\033[34m'
magenta='\033[35m'
cyan='\033[36m'
reset='\033[0m'

# Setup argparse for command line arguments
parser = argparse.ArgumentParser(description='RoboPet - A robotic pet project using iRobot Create 2 and OpenCV for computer vision.')
parser.add_argument('--port', type=str, default='/dev/ttyUSB0', help='Serial port for iRobot Create 2 (default: /dev/ttyUSB0)')
parser.add_argument('--baud', type=int, default=115200, help='Baud rate for serial communication (default: 115200)')
parser.add_argument('--logfile', type=str, default=logfile, help="Log file for sensor data (default: logfile)")
args = parser.parse_args()

logfile=args.logfile

# Setup logging. Check for existence of logfile and create if it doesn't exist
if not os.path.exists(logfile):
    print(f"Creating new logfile: {logfile}")
    with open(logfile, 'w') as f:
        f.write('================ RoboPet New LogFile ====================\n')
        f.close()

logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('Parser: Port=%s, Baud=%d, Logfile=%s', args.port, args.baud, args.logfile)
logging.info("\n")
logging.info('\n============== RoboPet Logging Started ==============')

# Setup CV2 version and load a cascade classifier for object detection
print(cv2.__version__)
logging.info('CV: Version %s', cv2.__version__)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Setup & Initialize curses environment
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
logging.info('Curses: Curses initialized...')

def get_roomba_data(bot):
    try:
        sensors = bot.get_sensors()
    except Exception as e:
        logging.info('Exception: %s', e)
        logging.info('Exception: Be sure to cleanly stop bot')
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(2)
        bot.stop()
        time.sleep(2.0)
        exit()
    else:
        logging.info('PyCreate: No Bot Exceptions, moving on.')
    finally:
        # Print sensor data
        sensors.wall == sensors[1]
        sensors.battery_charge == sensors[17]
        sensors.battery_capacity == sensors[18]
        sensors.charger_state == sensors[13]
        sensors.charger_available == sensors[24]
        sensors.temperature == sensors[16]
        # Print sensor data & Vacuum Telemetry data
        screen.addstr(20, 0, f"Wall Sensor: {sensors.wall}")
        screen.addstr(21, 0, f"Charger State: {sensors.charger_state}")
        screen.addstr(22, 0, f"Charger Available: {sensors.charger_available}")
        screen.addstr(23, 0, f"Battery Charge: {sensors.battery_charge}")
        screen.addstr(24, 0, f"Battery Capacity: {sensors.battery_capacity}")
        screen.addstr(25, 0, f"Temperature: {sensors.temperature}")
        logging.info('PyCreate: Get Sensors Complete')
        logging.info('PyCreate: Wall Sensor: %s%s%s', cyan, sensors.wall, reset)
        logging.info('PyCreate: Charger State: %s', sensors.charger_state)
        logging.info('PyCreate: Charger Available: %s', sensors.charger_available)
        logging.info('PyCreate: Battery Charge: %s', sensors.battery_charge)
        logging.info('PyCreate: Battery Capacity: %s', sensors.battery_capacity)
        logging.info('PyCreate: Temperature: %s', sensors.temperature)

    return


if __name__ == "__main__":
    # Create a Create2 bots settings
    port = '/dev/ttyUSB0'
    baud = { 'default': 115200 }
    logging.info('PyCreate: Port set to %s and baud rate set to %d', port, baud['default'])

    # Create video
    cap = cv2.VideoCapture(0)
    logging.info('CV: Camera initialized for CV')
    ret, frame = cap.read()
    if ret:
        screen.addstr(0, 0, 'Camera working correctly')
        msg=f"Frame shape: {frame.shape}"
        screen.addstr(1,0, msg)
        cv2.imshow('Captured', frame)
        logging.info('CV: Frame Captured')
        cv2.imwrite('Captured1.png', frame)
        logging.info('CV: Frame saved to file')
        # Load an image from a file
        img = cv2.imread('Captured1.png')
        logging.info('CV: Image loaded for facial recognition "FR"')
        # Convert image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # Iterate over the faces and draw rectangles around them
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255,0), 2)
        # Display the output image
        cv2.imshow('Output Image', img)
        logging.info('CV: Displaying image with FR squares')
        cv2.waitKey(0)
        #cv2.destroyWindow('Captured')
    else:
        msg=f"Failed to capture image."
        screen.addstr(1,20, msg)

    logging.info('CV: Cleanly releasing capture device')
    cap.release()
    logging.info('CV: CV2 cleanup and window destruction')
    cv2.destroyAllWindows()

    # Create and Initialize Roomba Create2
    try:
        bot = pycreate2.Create2(port=port, baud=baud['default'])
    except Exception as e:
        logging.info('PyCreate - Exception: %s', e)
        logging.info('PyCreate - Exception: No PyCreate Bot attached. Shutting down cleanly.')
        screen.addstr(20, 0, 'No PyCreate Bot attached.')
        logging.info('Curses - Exception: Cleanly shutting down Curses.')
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(0.5)
        os._exit(1)

    # Start the Create 2
    bot.start()
    bot.safe()      # Put the Create2 into 'safe' mode so we can drive it. This will still provide some protection
    time.sleep(0.5)
    bot.full()      # You are responsible for handling issues, no protection/safety in this mode ... be careful

    # Roomba is initialized, get data.
    get_roomba_data(bot)

    # Control the bot with keyboard input
    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                screen.addstr(30, 0, '**Quitting...**')
                logging.info('PyCreate - Input: Quitting')
                time.sleep(1.0)
                break
            elif char == curses.KEY_UP:
                screen.addstr(5, 0, 'up ')
                logging.info('PyCreate - Input: Up')
                bot.drive_direct(50,50)
                time.sleep(2.0)
                bot.drive_stop()
                get_roomba_data(bot)
            elif char == curses.KEY_RIGHT:
                screen.addstr(5, 0, 'right ')
                logging.info('PyCreate - Input: Right')
                bot.drive_direct(-25,25)
                time.sleep(2.0)
                bot.drive_stop()
                get_roomba_data(bot)
            elif char == curses.KEY_DOWN:
                screen.addstr(5, 0, 'down ')
                logging.info('PyCreate - Input: Down')
                bot.drive_direct(-50,-50)
                time.sleep(2.0)
                bot.drive_stop()
                get_roomba_data(bot)
            elif char == curses.KEY_LEFT:
                screen.addstr(5, 0, 'left ')
                logging.info('PyCreate - Input: Left')
                bot.drive_direct(25,-25)
                time.sleep(2.0)
                bot.drive_stop()
                get_roomba_data(bot)
    except Exception as e:
        # Shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(1)
        bot.stop()
    
    # Cleanup and shutdown the bot and curses environment
    logging.info('Exit: Shutting down bot and curses environment')
    print('Bot drive stop')
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    bot.drive_stop()
    time.sleep(0.1)
    print('Bot close')
    #bot.close()

