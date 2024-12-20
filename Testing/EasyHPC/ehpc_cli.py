#!/usr/bin/python3

from colorama import Fore, Back, Style
from ehpc_cluster import Cluster

# https://click.palletsprojects.com/en/8.1.x/
# https://geekyhumans.com/how-to-create-cli-in-python/
import click
# https://dev.pythonlibrary.org/2021/09/30/sqlite/
import sqlite3

# Initialize the environment
ehpc_db_file = 'ehpc.db'
sql_con = sqlite3.connect(ehpc_db_file)
sql_cur = sql_con.cursor()

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
    # Check for the existence of SQL tables
    # https://www.w3schools.com/python/python_try_except.asp
    try:
        #sql = 'SELECT name FROM sqlite_master WHERE name="cluster"'
        sql = 'SELECT * FROM cluster'
        res = sql_cur.execute(sql)
        if not res.fetchall():
            print('Cluster is empty, please create a new cluster with `ehpc cluster create <cluster name>`')
        else:
            print('TODO: Fix check for empty table')
    except sqlite3.OperationalError:
        print("DB %s not found. Creating a new one.", ehpc_db_file)
        init_cluster_db()
    except:
        print('Unhandled generic exception.')
    #finally:
    #    sql_con.commit()

def init_cluster_db():
    # https://www.sqlitetutorial.net/sqlite-create-table/
    sql = 'CREATE TABLE cluster (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, datacenter TEXT NOT NULL, login BOOLEAN NOT NULL, scheduler BOOLEAN NOT NULL, active BOOLEAN NOT NULL)'
    sql_cur.execute(sql)

@cluster.command()
def status():
    """Show cluster status"""
    click.echo('Show cluster status')
    #if cluster_exists():
    if 5 > 2:
        sql = 'SELECT active from cluster;'
        try:
            res = sql_cur.execute(sql)
            print(res.fetchall())
        finally:
            print('Ok')

@cluster.command()
def list():
    """List created clusters"""
    click.echo('Listing created clusters:')
    #if cluster_exists():
    if 5 > 2:
        sql = 'SELECT name from cluster;'
        res = sql_cur.execute(sql)
        print(res.fetchall())

@cluster.command('create')
@click.argument('name')
def create(name):
    """Create cluster"""
    print("Creating cluster {}".format(name))
    #sql = "INSERT INTO cluster VALUES(1, bob, 'Phillipsburg, False, False, False)"
    sql = "INSERT INTO cluster (name,datacenter,login,scheduler,active) VALUES ('{}','Phillipsburg', False, False, False)".format(name)
    try:
        res = sql_cur.execute(sql)
        print(res.fetchone())
        sql_con.commit()
    except sqlite3.IntegrityError:
        print("Name {} most likely not unique. Check for uniqness and try create command again.".format(name))
    except Exception as e:
        print("Unhandled generic exception: {}".format(e))
    #finally:

@ehpc_cli.group()
def login():
    """All comannds related to logins"""

@login.command()
def status():
    # TODO: Check cluster for login status then proceed likewise.
    pass

@ehpc_cli.group()
def compute():
    """All comannds related to computes"""

@ehpc_cli.group()
def scheduler():
    """All comannds related to schedulers"""

@ehpc_cli.group()
def status():
    """All comannds related to Global system status"""
    # Check for active clusters.
    if db_check_cluster_status():
        print('Cluster bob is active')
    else:
        print('No active cluster')
    return

def db_check_cluster_status(sql_conn):
    # TODOD: Check that at least on cluster exists and determine it's status
    sql = 'SELECT * from CLUSTER where...'
    return


#pcluster = Cluster('picamera')

if __name__ == '__main__':

    ehpc_cli(prog_name='ehpc')
