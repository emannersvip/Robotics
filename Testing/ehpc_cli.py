#!/usr/bin/python3

from colorama import Fore, Back, Style
from ehpc_cluster import Cluster

# https://click.palletsprojects.com/en/7.x/
# https://geekyhumans.com/how-to-create-cli-in-python/
import click
# https://dev.pythonlibrary.org/2021/09/30/sqlite/
import sqlite3

# Initialize the environment
sql_conn = sqlite3.connect('ehpc.db')

@click.group()
def ehpc_cli():
    """The eHPC CLI"""

@ehpc_cli.group()
def cluster():
    """All comannds related to clusters"""
    # If at least one cluster exists operate normally 
    # Else badger/notify the user of the cluster's inactive status and remediation steps.
    #   I.e.Create a login and scheduler node.
    # Initialize cluster DB if not already initilaized
    init_cluster_db()

def init_cluster_db():
    sql = 'CREATE TABLE cluster (id INTEGER, name TEXT, datacenter TEXT, login BOOLEAN, scheduler BOOLEAN, active BOOLEAN)'
    sql_conn.execute(sql)

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

def db_check_cluster_status(sql_conn):
    # TODOD: Check that at least on cluster exists and determine it's status
    sql = 'SELECT * from CLUSTER where...'
    return


#pcluster = Cluster('picamera')

if __name__ == '__main__':
    ehpc_cli(prog_name='ehpc')
