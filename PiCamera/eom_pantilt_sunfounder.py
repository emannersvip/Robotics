#!/usr/bin/env python3

import curses

from servo import Servo
from time import sleep

pan  = Servo(pin=13, max_angle=90, min_angle=-90)
#pan  = Servo(pin=13)
tilt = Servo(pin=12, max_angle=30, min_angle=-90)
#tilt = Servo(pin=12)

def main():
    #while True:
    #    print(f"Bob is here")
    #    pan.set_angle(10)
    #    sleep(2)
    #    tilt.set_angle(10)
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    screen.addstr(1,  2, 'Press    to QUIT' )
    screen.addstr(1,  8, '\'Q\'', curses.A_BLINK )
    screen.addstr(2,  2, 'Press \'D\' to get DEBUG info' )

    screen.addstr(5,  2, '===============================================')
    screen.addstr(6,  2, '#                Pan Tilt Controls            #')
    screen.addstr(7,  2, '# URL: ssh://pi-robot-2.edsonmanners.com:8000 #')
    screen.addstr(8,  2, '#                                             #')
    screen.addstr(9,  2, '#                                             #')
    screen.addstr(10, 2, '#                    Up                       #')
    screen.addstr(11, 2, '#               Left    Right                 #')
    screen.addstr(12, 2, '#                   Down                      #')
    screen.addstr(13, 2, '#                                             #')
    screen.addstr(14, 2, '#                                             #')
    screen.addstr(15, 2, '#                                             #')
    screen.addstr(16, 2, '# URL: http://192.168.68.24:8888              #')
    screen.addstr(17, 2, '# URL: http://192.168.68.24:8888              #')
    screen.addstr(18, 2, '===============================================')
    sleep(5)
    #--
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nCanceled by User.')
