#!/usr/bin/python3
# iRobotCreate 2 controls

import pycreate2
import time

if __name__ == "__main__":
    # Create a Create2 bot
    port = '/dev/ttyUSB0'
    baud = { 'default': 115200 }

    bot = pycreate2.Create2(port=port, baud=baud['default'])

    # Define a movement path
    path = [
        [ 200, 200, 3, 'for'],
        [-200,-200, 3, 'back'],
        [   0,   0, 1, 'stop'],
        [ 100,   0, 2, 'rite'],
        [   0, 100, 4, 'left'],
        [ 100,   0, 2, 'rite'],
        [   0,   0, 1, 'stop'],
    ]

    bot.start()

    # Path to move
    for lft, rht, dt, s in path:
        print(s)
        bot.digit_led_ascii(s)
        bot.drive_direct(lft, rht)
        time.sleep(dt)
    
    bot.stop()
    print('Shutting down ... bye')
    bot.drive_stop()
    time.sleep(0.1)

