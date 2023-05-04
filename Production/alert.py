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

import logging
import os
import subprocess
import sys
import time

# https://pypi.org/project/discord-webhook/
from discord_webhook import DiscordWebhook

# Functions
def send_alert():
    print('Send alert')
    response = webhook.execute()
    return

logfile = '/home/emanners/Code/Production/alert_log.log'
# Setup logging of alerts
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s')
# Print timestamp everytime we start the program
logging.info(' ================= Program BEGIN ======================')

webhook_url = 'https://discord.com/api/webhooks/1103493285705687101/nfzsLa2zGyQaXCYCMN9NuoD9xaWNpCfEe4ARiYKaOe_h34sNKbu_WCyPDtZyuFg6x8HJ'
#webhook_content = 'EOM Webhook Message'
webhook_content = ':alarm_clock: Philipsburg Rear: Motion Detected'
webhook_username = ':alarm_clock: Philipsburg Rear: Motion Detected'
#webhook = DiscordWebhook(url=webhook_url, content=webhook_content)
webhook = DiscordWebhook(url=webhook_url, username=webhook_username)
with open('/motion/lastsnap.jpg', 'rb') as f:
	webhook.add_file(file=f.read(), filename='snapshot.jpg')
#response = webhook.execute()

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


