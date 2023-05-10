#!/usr/bin/python3
#---------------------------------------------------------------
#
# TODO:
# -- Send an alert to discord
# -- Email latest snapshot
# *- Setup systemd service in Ansible
#
# Author: Edson Manners, 2023
#
# Version: 01.1rc
#
#---------------------------------------------------------------

import datetime
import logging
import os
import subprocess
import sys
import time

# https://pypi.org/project/discord-webhook/
from discord_webhook import DiscordWebhook

# Functions
def send_alert():
    print('Sent alert at: ' + str(datetime.datetime.now()))
    webhook_last_pic = get_last_photo()
    with open(webhook_last_pic, 'rb') as f:
       	webhook.add_file(file=f.read(), filename='lastphoto.jpg')
    response = webhook.execute()
    return

def get_last_photo():
    #print('Send photo')
    search_string = 'phillip'
    # Get list of all photos in reverse chronological order
    result = subprocess.run(['ls', '-larth', '/motion/photo'], capture_output=True)
    # Split into a new-line separated list
    last_list = result.stdout.decode().splitlines()
    tmp_list = []
    # Remove current '.' and parent '..' directory listings if they're the last entries.
    # find() returns the index of the substr position, -1 if *NOT* found.
    for i in range(len(last_list)):
        if last_list[i].find(search_string) != -1:
            #print('AA ' + last_list[i])
            continue
        else:
            #print('XX ' + last_list[i])
            tmp_list.append(i)
    # Now pop the un-needied entries ow that we're no longer iterating through the list that
    # we're changing. Reverse the list so the pop operation doesn't mess up the indices.
    tmp_list.reverse()
    for i in tmp_list:
        last_list.pop(i)
    # Return the eight entry (filename) of the last entry (latest photo) in the array
    latest_photo = '/motion/photo/' + last_list[-1].split()[8]
    print('Sent latest photo: ' + latest_photo)
    return latest_photo

logfile = '/home/emanners/Code/Production/alert_log.log'
# Setup logging of alerts
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
# Print timestamp everytime we start the program
logging.info(' ================= Program BEGIN ======================')

webhook_url = 'https://discord.com/api/webhooks/1103493285705687101/nfzsLa2zGyQaXCYCMN9NuoD9xaWNpCfEe4ARiYKaOe_h34sNKbu_WCyPDtZyuFg6x8HJ'
webhook_content = ':alarm_clock: Philipsburg Rear: Motion Detected'
webhook_username = ':alarm_clock: Philipsburg Rear: Motion Detected'
webhook_last_pic = ''
webhook = DiscordWebhook(url=webhook_url, username=webhook_username)

# Previous directory listing file
prev_file = '/tmp/motion_diff1'
next_file = '/tmp/motion_diff2'
# Default will be 5 minutes (300 seconds)
sleep_time = 300

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


