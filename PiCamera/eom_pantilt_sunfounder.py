#!/usr/bin/env python3

# https://docs.python.org/3/howto/curses.html
import curses

from curses import wrapper
from servo import Servo
from time import sleep

pan  = Servo(pin=13, max_angle=90, min_angle=-90)
tilt = Servo(pin=12, max_angle=30, min_angle=-90)

def main(stdscr):
    pan_angle = 0
    tilt_angle = 0
    stdscr.clear()

    stdscr.addstr(1,  2, 'Press     to QUIT' )
    stdscr.addstr(1,  8, '\'Q\'', curses.A_BLINK )
    stdscr.addstr(2,  2, 'Press \'D\' to get DEBUG info' )

    stdscr.addstr(5,  2, '======================================')
    stdscr.addstr(6,  2, '#         Pan Tilt Controls          #')
    stdscr.addstr(7,  2, '# URL: ssh://192.168.68.24:22        #')
    stdscr.addstr(8,  2, '#                                    #')
    stdscr.addstr(9,  2, '#                                    #')
    stdscr.addstr(10, 2, '#                Up                  #')
    stdscr.addstr(11, 2, '#           Left    Right            #')
    stdscr.addstr(12, 2, '#               Down                 #')
    stdscr.addstr(13, 2, '#                                    #')
    stdscr.addstr(14, 2, '#                                    #')
    stdscr.addstr(15, 2, '#                                    #')
    stdscr.addstr(16, 2, '# URL: http://192.168.68.24:8000     #')
    stdscr.addstr(17, 2, '# URL: http://24.229.161.67:8000     #')
    stdscr.addstr(18, 2, '======================================')

    stdscr.refresh()
    stdscr.getkey()

    try:
        while True:
            char = stdscr.getch()
            if char == ord('q'):
                break
            if char == ord('d'):
                pass
            elif char == curses.KEY_RIGHT:
                stdscr.addstr(0, 0, 'right')
                pan_angle = pan_angle - 1
                pan.set_angle(pan_angle)
                print(f"Pan Angle: {pan_angle}")
            elif char == curses.KEY_LEFT:
                stdscr.addstr(0, 0, 'left')
                pan_angle = pan_angle + 1
                pan.set_angle(pan_angle)
                print(f"Pan Angle: {pan_angle}")
            elif char == curses.KEY_UP:
                stdscr.addstr(0, 0, 'up')
                tilt_angle = tilt_angle - 1
                tilt.set_angle(tilt_angle)
                print(f"Tilt Angle: {tilt_angle}")
            elif char == curses.KEY_DOWN:
                stdscr.addstr(0, 0, 'down')
                tilt_angle = tilt_angle + 1
                tilt.set_angle(tilt_angle)
                print(f"Tilt Angle: {tilt_angle}")
            else:
                stdscr.addstr(0, 0, 'Not currently supported')
    finally:
        # Shutdown cleanly
        curses.nocbreak(); stdscr.keypad(0); curses.echo()
        curses.endwin()

    return
    

wrapper(main)

#if __name__ == '__main__':
#    try:
#        main()
#        print(f"End main")
#    except KeyboardInterrupt:
#        print('\nCanceled by User.')
