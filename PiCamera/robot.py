#!/usr/bin/python3
#
# https://picamera.readthedocs.io/en/release-1.13/recipes1.html#recipes1
# https://core-electronics.com.au/guides/pan-tilt-hat-raspberry-pi/
# https://learn.pimoroni.com/article/assembling-pan-tilt-hat

from time import sleep

from picamera2 import Picamera2
#import pantilthat


camera = Picamera2()

camera.resolution = (1024, 768)
camera.start_preview()

#Camera warm-up time
sleep(2)
camera.capture('foo.jpg')

