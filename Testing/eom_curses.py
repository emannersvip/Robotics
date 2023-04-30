#!/usr/bin/python3

import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    #pass

    # This raises a ZeroDivisionError when i == 10.
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    # Place computer game controls on the left
    # Left buttons are for body motion, i.e. the Roomba
    stdscr.addstr(12, 12, 'W')
    stdscr.addstr(13, 10, 'A')
    stdscr.addstr(14, 12, 'S')
    stdscr.addstr(13, 14, 'D')

    # Place directional controls on the right
    # Right keys are for looking, i.e. the Pimorino camera tilt/pan
    stdscr.addstr(12, 33, 'Up')
    stdscr.addstr(13, 28, 'Left')
    stdscr.addstr(14, 32, 'Down')
    stdscr.addstr(13, 36, 'Right')

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)


