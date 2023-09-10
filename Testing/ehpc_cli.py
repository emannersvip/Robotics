#!/usr/bin/python3

# https://click.palletsprojects.com/en/7.x/
# https://geekyhumans.com/how-to-create-cli-in-python/

from colorama import Fore, Back, Style
from ehpc_cluster import Cluster

import click
import sqlite3

# Initialize the environment
sqlite3.connect('ehpc.db')

@click.group()
def ehpc_cli():
    """The eHPC CLI"""

@ehpc_cli.group()
def cluster():
    """All comannds related to clusters"""
    # If at least one cluster exists operate normally 
    # Else badger/notify the user of the cluster's inactive status and remediation steps.
    #   I.e.Create a login and scheduler node.

@ehpc_cli.group()
def login():
    """All comannds related to logins"""

@ehpc_cli.group()
def compute():
    """All comannds related to computes"""

@ehpc_cli.group()
def scheduler():
    """All comannds related to schedulers"""

@ehpc_cli.group()
def status():
    """All comannds related to Global system status"""

#pcluster = Cluster('picamera')

if __name__ == '__main__':
    ehpc_cli(prog_name='ehpc')
