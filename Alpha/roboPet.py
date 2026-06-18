#!/usr/bin/env python3
# iRobotCreate 2 controls
# Send to dock:
# -- https://github.com/iRobotSTEM/CreatePython/blob/main/Create2_TetheredDrive.py

import curses
import cv2
import logging
import numpy as np
import os
import time

import pycreate2

# Set environment variables
os.environ['QT_QPA_PLATFORM']='xcb'

# Print CV2 version and load a cascade classifier for object detection
print(cv2.__version__)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

logfile='/home/emanners/Documents/Git/Robotics/Alpha/sensor.log'
#logfile='/home/emanners/Code/Robotics/iRobotCreate2/sensor.log'
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
logging.info("\n")
logging.info('\n============== RoboPet Logging Started ==============')

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
logging.info('Curses: curses initialized...')

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
    #img = cv2.imread('/home/emanners/Pictures/Screenshots/Screenshot From 2026-02-22 07-40-18.png')
    #cv2.imshow('Output', img)
    #cv2.waitKey(0)
    logging.info('CV: CV2 cleanup and window destruction')
    cv2.destroyAllWindows()

    # Create a Create 2
    try:
        bot = pycreate2.Create2(port=port, baud=baud['default'])
    except Exception as e:
        logging.info('PyCreate - Exception: %s', e)
        logging.info('PyCreate - Exception: No PyCreate Bot attached. Shutting down cleanly.')
        screen.addstr(20, 0, 'No PyCreate Bot attached.')
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        time.sleep(0.5)
        os._exit(1)

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
                screen.addstr(5, 0, 'up ')
                bot.drive_direct(50,50)
                time.sleep(2.0)
                bot.drive_stop()
            elif char == curses.KEY_RIGHT:
                screen.addstr(5, 0, 'right ')
                bot.drive_direct(-25,25)
                time.sleep(2.0)
                bot.drive_stop()
            elif char == curses.KEY_DOWN:
                screen.addstr(5, 0, 'down ')
                bot.drive_direct(-50,-50)
                time.sleep(2.0)
                bot.drive_stop()
            elif char == curses.KEY_LEFT:
                screen.addstr(5, 0, 'left ')
                bot.drive_direct(25,-25)
                time.sleep(2.0)
                bot.drive_stop()
    except Exception as e:
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

