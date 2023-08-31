from picamera2 import Picamera2
import picamera

import socket

# Setup web socket
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostbyname('raspberrypi')
host = 'raspberrypi'
port = 8000
#s.connect((host, port))
conn = s.makefile('wb')

with picamera.PiCamera(resolution='VGA', framerate=15) as camera:
    camera.start_recording(ouput, format='mjpeg')
    camera.wait_recording(30)
    camera.stop_recording()

conn.close()
s.close()