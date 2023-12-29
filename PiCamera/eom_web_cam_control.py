# https://stackoverflow.com/questions/48552343/how-can-i-execute-a-python-script-from-an-html-button
# Bringing in code from eom_camera_control

from flask import Flask, render_template
from servo import Servo
from time import sleep

pan  = Servo(pin=13, max_angle=90, min_angle=-90)
tilt = Servo(pin=12, max_angle=30, min_angle=-90)
#global pan_angle
#global tilt_angle
pan_angle = 0
tilt_angle =0

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left')
def left():
    print('Left arrow clicked')
    global pan_angle
    pan_angle = pan_angle + 1
    pan.set_angle(pan_angle)
    #return 'Click.'
    return render_template('index.html')

@app.route('/right')
def right():
    print('Right arrow clicked')
    global pan_angle
    pan_angle = pan_angle - 1
    pan.set_angle(pan_angle)
    return render_template('index.html')

@app.route('/up')
def up():
    print('Up arrow clicked')
    global tilt_angle
    tilt_angle = tilt_angle - 1
    tilt.set_angle(tilt_angle)
    return render_template('index.html')

@app.route('/down')
def down():
    print('Down arrow clicked')
    global tilt_angle
    tilt_angle = tilt_angle + 1
    tilt.set_angle(tilt_angle)
    return render_template('index.html')

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    main()
