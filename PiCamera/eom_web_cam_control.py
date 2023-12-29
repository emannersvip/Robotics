# https://stackoverflow.com/questions/48552343/how-can-i-execute-a-python-script-from-an-html-button
# Bringing in code from eom_camera_control

from flask import Flask, render_template
from servo import Servo
#from time import sleep

# TODO:
# - Add check for joystick cam control

pan_angle = 0
tilt_angle = 0
pan_angle_max = 90
pan_angle_min = -90
tilt_angle_max = 30
tilt_angle_min = -30
motion_diff = 5
pan  = Servo(pin=13, max_angle=pan_angle_max, min_angle=pan_angle_min)
tilt = Servo(pin=12, max_angle=tilt_angle_max, min_angle=tilt_angle_min)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left')
def left():
    global pan_angle, pan_angle_max
    print(f"Left arrow clicked: {pan_angle}")
    if pan_angle < pan_angle_max:
        pan_angle = pan_angle + motion_diff
        pan.set_angle(pan_angle)
    else:
        print(f"At MAX angle {pan_angle_max}")
    #return 'Click.'
    return render_template('index.html')

@app.route('/right')
def right():
    global pan_angle, pan_angle_min
    print(f"Right arrow clicked: {pan_angle}")
    if pan_angle > pan_angle_min:
        pan_angle = pan_angle - motion_diff
        pan.set_angle(pan_angle)
    else:
        print(f"At MIN angle {pan_angle_min}")
    return render_template('index.html')

@app.route('/up')
def up():
    global tilt_angle, tilt_angle_min
    print(f"Up arrow clicked: {tilt_angle}")
    if tilt_angle > tilt_angle_min:
        tilt_angle = tilt_angle - motion_diff
        tilt.set_angle(tilt_angle)
    else:
        print(f"At MIN angle {tilt_angle_min}")
    return render_template('index.html')

@app.route('/down')
def down():
    global tilt_angle, tilt_angle_max, tilt_angle_min
    print(f"Down arrow clicked: {tilt_angle}")
    if tilt_angle < tilt_angle_max:
        tilt_angle = tilt_angle + motion_diff
        tilt.set_angle(tilt_angle)
    else:
        print(f"At MAX angle {tilt_angle_max}")
    return render_template('index.html')

def main():
    app.run(host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main()
