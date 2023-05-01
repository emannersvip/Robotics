#!/usr/bin/python3
#---------------------------------------------------------------
#
# TODO:
# -- Send an alert to discord
# -- Email latest snapshot
# Author: Edson Manners, 2023
#
#---------------------------------------------------------------

import os
import subprocess
import sys
import time

def send_alert():
    print('Send alert')
    print(result.stdout.decode())
    return

# Previous directory listing file
prev_file = '/tmp/motion_diff1'
next_file = '/tmp/motion_diff2'
# Default will be 5 minutes (300 seconds)
sleep_time = 120

try:
    while(True):
        # Get current directory listing data
        result = subprocess.run(['ls', '-lh', '/motion/'], capture_output=True)

        # If previous directory listing data exists, comapre it.
        if os.path.exists(prev_file):
            # read in file contents and compare.
            file1 = open(prev_file, 'r')
            file2 = open(next_file, 'w')
            file2.writelines(result.stdout.decode())
            file2.close()
            file2 = open(next_file, 'r')
            prev_listing = file1.read()
            next_listing = file2.read()
            file1.close() ; file2.close()
            # Check for changes/new files in directory.
            # If there aren't any changes, sleep and try again later
            if next_listing == prev_listing:
                #print('Next')
                next
            # If there are changes, send an alert and update the directory listing refreence file
            else:
                #print('Changed')
                send_alert()
                file1 = open(prev_file, 'w')
                file1.writelines(result.stdout.decode())
                file1.close()
        else:
            # Else create 'previous' file and try again in the next iteration of the loop.
            file1 = open(prev_file, 'w')
            # Convert and save binary string output to regular string.
            print('Can\'t find: ' + prev_file + '\n Making a new one.')
            file1.writelines(result.stdout.decode())
            file1.close()
        time.sleep(sleep_time)
except KeyboardInterrupt:
    # Quit cleanly
    print('Shutting down! c')
    sys.exit()
finally:
    print('Shutting down! s')


