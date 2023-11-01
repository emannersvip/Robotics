#!/usr/bin/python3

#import sqlite3
import shelve
# https://the-examples-book.com/programming-languages/python/argparse
# https://docs.python.org/3/library/argparse.html
import argparse

from ehpc_cluster import Cluster
#from ehpc_login_node import LoginNode
from ehpc_colors import eColors

# TODO:
# - Do a check on arg[0]
# - Add a debug option to arg[0]

cluster_name = 'Default Cluster'
# DEBUG CODE
debug = 1
if debug:
    dc = '000: '
else:
    dc =''

mychoices = ['cluster', 'debug', 'login', 'status']

# Do error checking on this later
# TODO: check if file exists
# 2) check for cluster, login, etc and load appropriately.
sh = shelve.open('ehpc.shelf')

# In the future this is not needed as we can simplyt just use the .get() method instead
try:
    myCluster = sh['cluster']
except KeyError:
    print(f"It's fine we just won't load a Cluster here")
try:
    myLogin = sh['loginnode']
except KeyError:
    print(f"It's fine we just won't load a LoginNode here")
try:
    myCompute = sh['computenode']
except KeyError:
    print(f"It's fine we just won't load a ComputeNode here")


def getClusterStatus():
    myCluster.get_status()
    return

def createCluster(name):
    return myCluster.create_cluster(name)

if __name__ == "__main__":
    print(f"{dc} Welcome to Easy HPC:")
    parser = argparse.ArgumentParser(description='List data from a database')
    parser.add_argument('object1',
                        help='Primary argument object is a Noun. See choices',
                        #choices=['cluster','compute','login','scheduler','status'],
                        nargs='+',
                        type=str)
    #parser.add_argument('-d', '--debug', help='Adds helpful debug output')
    #parser.add_argument('-v', '--version', help='Version 0.1a')

    args = parser.parse_args()

    if args.object1 and len(args.object1) >= 1:
        # Check that a cluster exists and promt to create one if not
        try:
            myCluster
        except NameError:
            myCluster = None
            print(f"{dc} No {eColors.CYAN}cluster{eColors.ENDC} exists. Initiaize EasyHPC now? (Y/n): ")
            einit = input()

            if einit != 'n' or einit != 'N':
                print(f"{dc} Please provide {eColors.CYAN}CLUSTER{eColors.ENDC} name <{cluster_name}>: ")
                # Use a sanitizing funtion later
                cluster_name = input()
                if len(cluster_name) > 1:
                    myCluster = Cluster(cluster_name)
                    sh['cluster'] = myCluster
                    sh.sync()
                    sh.close()
                    exit()
                else:
                    # Complain
                    print(f"{dc}Bad cluster name")

        if args.object1[0] == 'cluster':
            print(args.object1)
            if args.object1[1] == 'status':
                getClusterStatus()
            elif args.object1[1] == 'create' and args.object1[2]:
                myLoginNode = createCluster(args.object1[2])
                print(f"{dc}Login: {myLoginNode}")
                sh['loginnode'] = myLoginNode
                sh['cluster'] = myCluster
                sh.sync()
            else:
                print(f"{eColors.CYAN}ehpc{eColors.ENDC}->{eColors.CYAN}cluster{eColors.ENDC}->{eColors.RED}{args.object1[1]}{eColors.ENDC} not yet supported!\n")
            pass
        elif args.object1[0] == 'login':
            # Check cluster status and/or datacenter status in the future
            print(f"Checking Login Nodes.")
            if sh.get('loginnode') != None:
                if args.object1[1] == 'status':
                    print(f"{eColors.CYAN}Login Node{eColors.ENDC} {eColors.GREEN}" + sh.get('loginnode').getName() + f"{eColors.ENDC} exists.")
                elif args.object1[1] == 'list':
                    print(f"{eColors.CYAN}Login Nodes:{eColors.ENDC}")
                    myLoginNode = sh.get('loginnode')
                    print(f"  Name: {eColors.GREEN}" + myLoginNode.getName() + f"{eColors.ENDC}")
                    if myLoginNode.validateNode() and sh.get('computenode') == None:
                            sh['addCompute'] = True
                else:
                    print(f"{args.object1[1]} is not a supported option.")
        elif args.object1[0] == 'status':
            # Check cluster status and/or datacenter status in the future
            print(f"Checking eHPC status.")
        elif args.object1[0] == 'debug':
            # Check cluster status and/or datacenter status in the future
            try:
                print(f"\n{dc}Updated Data = {sh['cluster']}")
                print(f"{dc}Updated Data = {sh['loginnode']}")
            except KeyError as ke:
                print(f"{dc} Shelf key {eColors.CYAN}{ke}{eColors.ENDC} does not exist!")
            finally:
                print(f"{dc}Debug complete!\n")
        else:
            print(f"{dc}If {args.object1} Unkknown query. Valid entries are: {mychoices}")
    else:
        print(f"{dc}eHPC ran with no argument!!!")

sh.sync()
sh.close()

