#!/usr/bin/env python3

from servo import Servo
from time import sleep

pan  = Servo(pin=13, max_angle=90, min_angle=-90)
#pan  = Servo(pin=13)
tilt = Servo(pin=12, max_angle=30, min_angle=-90)
#tilt = Servo(pin=12)

def main():
    while True:
        print(f"Bob is here")
        pan.set_angle(10)
        sleep(2)
        tilt.set_angle(10)
        #pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nCanceled by User.')
