## EOM ROBOTICS

# LIBCAMERA2

# iROBOT CREATE

# BLUETOOTH
#  https://raspberrytips.com/raspberry-pi-bluetooth-setup/
# https://raspberry-valley.azurewebsites.net/Map-Bluetooth-Controller-using-Python/
# evtest
python3 /usr/local/lib/python3.9/dist-packages/evdev/evtest.py
                               ^^

$ hciconfig

$ sudo bluetoothctl
Agent registered
[bluetooth]# power off
Changing power off succeeded
[bluetooth]# power on
Changing power on succeeded
[bluetooth]# devices
[bluetooth]# scan on
Discovery started
[CHG] Controller D8:3A:DD:3C:3F:E3 Discovering: yes
[NEW] Device EE:A8:41:4B:C3:12 NLFGW
[NEW] Device D6:DC:8A:5C:B6:DC NLRRE
[CHG] Device 78:F2:F1:10:A9:C4 RSSI: -64
[CHG] Device EE:A8:41:4B:C3:12 RSSI: -74
...
[NEW] Device 20:20:F8:28:18:6C ECOLOR_E0707F828
[NEW] Device 98:B6:E9:E2:0B:9D Pro Controller
[CHG] Device EE:A8:41:4B:C3:12 ServiceData Key: 0000feaf-0000-1000-8000-00805f9b34fb
[CHG] Device EE:A8:41:4B:C3:12 ServiceData Value:
  10 01 00 02 00 e1 08 00 90 eb 4c 64 00 66 16 64  ..........Ld.f.d
  01                                               .
[CHG] Device 20:20:F8:28:18:6C RSSI: -78
[bluetooth]# connect 98:B6:E9:E2:0B:9D
Attempting to connect to 98:B6:E9:E2:0B:9D
[CHG] Device 98:B6:E9:E2:0B:9D Connected: yes
[CHG] Device 98:B6:E9:E2:0B:9D Modalias: usb:v057Ep2009d0001
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001000-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001124-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device 98:B6:E9:E2:0B:9D ServicesResolved: yes
[CHG] Device D6:DC:8A:5C:B6:DC RSSI: -50
[CHG] Device 98:B6:E9:E2:0B:9D Paired: yes
Connection successful
[CHG] Device 78:F2:F1:10:A9:C4 RSSI: -46
[CHG] Device EE:A8:41:4B:C3:12 RSSI: -66
[Pro Controller]# pair 98:B6:E9:E2:0B:9D
Attempting to pair with 98:B6:E9:E2:0B:9D
Failed to pair: org.bluez.Error.AlreadyExists
[Pro Controller]# exit
