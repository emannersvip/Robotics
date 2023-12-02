# https://raspberry-valley.azurewebsites.net/Map-Bluetooth-Controller-using-Python/
from evdev import InputDevice, categorize, ecodes

# Button mappings
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 306

print(f"Switch Pro GamePad Mapping to Raspberry Pi with Bluetooth")

gamepad = InputDevice('/dev/input/event5')

print(gamepad)

for event in gamepad.read_loop():
    #print(categorize(event))
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == aBtn:
                print(f"A")
            elif event.code == bBtn:
                print(f"B")
            elif event.code == xBtn:
                print(f"X")
            elif event.code == yBtn:
                print(f"Y")
            else:
                print(categorize(event))


