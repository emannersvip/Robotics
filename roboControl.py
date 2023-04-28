# iRobotCreate 2 controls

import pycreate2

if __name__ == "__main__":
    # Create a Create2 bot
    port = '/dev/ttyUSB0'
    baud = { 'default': 115200 }

    bot = pycreate2.Create2(port=port, baud=baud['default'])

    # Define a movement path
    path = [
        [  20,  20, 3, 'for'],
        [ -20, -20, 3, 'back'],
        [   0,   0, 1, 'stop'],
        [  10,   0, 2, 'rite'],
        [   0,  10, 4, 'left'],
        [  10,   0, 2, 'rite'],
        [   0,   0, 1, 'stop'],
    ]

    bot.start()
    bot.stop()