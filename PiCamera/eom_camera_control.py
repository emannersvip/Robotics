#!/usr/bin/python3
# https://shop.pimoroni.com/en-us/products/pan-tilt-hat
# https://github.com/pimoroni/pantilt-hat/blob/master/examples/timeout.py
# https://core-electronics.com.au/guides/pan-tilt-hat-raspberry-pi/

# Importing required libraries
import curses
import os
import time

import pantilthat
import picamera

# Initialize camera
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
# Flipping the camera so it's not upside-down
camera.vflip = True
camera.hflip = True

#camera.start_preview(fullscreen=False, window = (100,20,640,480))
#camera.start_recording('video.h264')
#time.sleep(0.4)
#camera.stop_recording()

#pantilthat.idle_timeout(0.5)

# Set up key mappings and curses for arrow key responses
screen = curses.initscr()   # get the curses screen window
curses.noecho()             # turn off input echoing
curses.cbreak()             # respond to keys immediately (don't wait for enter)
screen.keypad(True)         # map arrow keys to special values

# initialize pan and tilt positions and process increments driven by arrow keys
# set start up servo positions
a = -37.0
b = -38.0
pantilthat.pan(a)       # TODO: Make this happen smootly
pantilthat.tilt(b)      # TODO: Make this happen smoothly
# set arrow key delta
deltaPan=1.0
deltaTilt=1.0

photoNum = 1    # Initialize photo number

# Process active key presses:
# -- Letter p will take a picture and store filename (until we get to controller)
#
# -- Arrow keys will control the Pan Tilt Camera (deltaPan/deltaTilt degree angles)
# -- Letter q will quit the application
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        if char == ord('p'):
            # if 'p' is pressed take a photo
            camera.capture('image%s.jpg' % photoNum)
            photoNum = photoNum + 1
            screen.addstr(0, 0, 'Photo Taken! ')
        elif char == ord('d'):
            # if 'd' is pressed print debug information
            screen.addstr(3, 0, 'Pan: ')
            screen.addstr(3, 5, str(a))
            screen.addstr(4, 0, 'Tilt: ')
            screen.addstr(4, 5, str(b))
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'Right ')
            if (a - deltaPan) > -90:
                a = a - deltaPan
            pantilthat.pan(a)
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'Left ')
            if (a - deltaPan) < 90:
                a = a + deltaPan
            pantilthat.pan(a)
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'Down ')
            if (b + deltaTilt) < 90:
                b = b + deltaTilt
            pantilthat.tilt(b)
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'Up ')
            if (b + deltaTilt) > -90:
                b = b - deltaTilt
            pantilthat.tilt(b)
            time.sleep(0.005)

finally:
    # shut down cleanly
    camera.stop_preview
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()



