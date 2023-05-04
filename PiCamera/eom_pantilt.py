#!/usr/bin/python3

# https://shop.pimoroni.com/en-us/products/pan-tilt-hat
# https://github.com/pimoroni/pantilt-hat/blob/master/examples/timeout.py
# https://core-electronics.com.au/guides/pan-tilt-hat-raspberry-pi/

import curses
import time

import pantilthat

pantilthat.idle_timeout(0.5)

# Set up key mappings and curses for arrow key responses
screen = curses.initscr()   # get the curses screen window
curses.noecho()             # turn off input echoing
curses.cbreak()             # respond to keys immediately (don't wait for enter)
screen.keypad(True)         # map arrow keys to special values

# initialize pan and tilt positions and process increments driven by arrow keys
# set start up servo positions
a = -23.0
b = -13.0

try:
    pantilthat.pan(a)       # TODO: Make this happen smootly
    pantilthat.tilt(b)      # TODO: Make this happen smoothly
except PermissionError as e:
    curses.nocbreak(); screen.keypad(0); curses.echo(); curses.endwin()
    print('Can\'t load the pantilt module. Please check the HW.')
    print(e)
    exit()

# set arrow key delta
deltaPan=1.0
deltaTilt=1.0


screen.addstr(1,  2, 'Press     to QUIT' )
screen.addstr(1,  8, '\'Q\'', curses.A_BLINK )
screen.addstr(2,  2, 'Press \'D\' to get DEBUG info' )

screen.addstr(5,  2, '======================================')
screen.addstr(6,  2, '#         Pan Tilt Controls          #')
screen.addstr(7,  2, '# URL: ssh://192.168.0.177:8022      #')
screen.addstr(8,  2, '#                                    #')
screen.addstr(9,  2, '#                                    #')
screen.addstr(10, 2, '#                Up                  #')
screen.addstr(11, 2, '#           Left    Right            #')
screen.addstr(12, 2, '#               Down                 #')
screen.addstr(13, 2, '#                                    #')
screen.addstr(14, 2, '#                                    #')
screen.addstr(15, 2, '#                                    #')
screen.addstr(16, 2, '# URL: http://192.168.0.177:8081     #')
screen.addstr(17, 2, '# URL: http://24.229.161.67:8081     #')
screen.addstr(18, 2, '======================================')

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
        if char == ord('d'):
            # if 'd' is pressed print debug information
            screen.addstr(3, 0, 'Pan: ')
            screen.addstr(3, 5, str(a))
            screen.addstr(4, 0, 'Tilt: ')
            screen.addstr(4, 5, str(b))
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right ')
            if (a - deltaPan) > -90:
                a = a - deltaPan
            pantilthat.pan(a)
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            if (a - deltaPan) < 90:
                a = a + deltaPan
            pantilthat.pan(a)
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            if (b + deltaTilt) < 90:
                b = b + deltaTilt
            pantilthat.tilt(b)
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up ')
            if (b + deltaTilt) > -90:
                b = b - deltaTilt
            pantilthat.tilt(b)
            time.sleep(0.005)

finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()



