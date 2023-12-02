
# https://pypi.org/project/pycreate2/

pip install pycreate2

Installing collected packages: simplejson, pyserial, colorama, pycreate2
  WARNING: The scripts pyserial-miniterm and pyserial-ports are installed in '/home/emanners/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts create_monitor, create_reset and create_shutdown are installed in '/home/emanners/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

$ sudo bluetoothctl
Agent registered
[bluetooth]# scan on
Discovery started
[CHG] Controller D8:3A:DD:3C:3F:E3 Discovering: yes
[NEW] Device 71:9B:83:1F:9F:AA 71-9B-83-1F-9F-AA
...
[NEW] Device 98:B6:E9:E2:0B:9D Pro Controller
[CHG] Device 98:B6:E9:E2:0B:9D RSSI: -71

[bluetooth]# connect 98:B6:E9:E2:0B:9D
Attempting to connect to 98:B6:E9:E2:0B:9D
[CHG] Device 98:B6:E9:E2:0B:9D Connected: yes
[CHG] Device 98:B6:E9:E2:0B:9D Modalias: usb:v057Ep2009d0001
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001000-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001124-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D ServicesResolved: yes
[CHG] Device 98:B6:E9:E2:0B:9D Paired: yes
Connection successful

emanners@pi-robot-2:~/Code/Robotics/iRobotCreate2 $ python3 /usr/local/lib/python3.9/dist-packages/evdev/evtest.py
ID  Device               Name                                Phys                                Uniq
------------------------------------------------------------------------------------------------------------------
0   /dev/input/event0    vc4-hdmi-0                          vc4-hdmi-0/input0
1   /dev/input/event1    vc4-hdmi-1                          vc4-hdmi-1/input0
2   /dev/input/event2    Pro Controller                      d8:3a:dd:3c:3f:e3                   98:b6:e9:e2:0b:9d
