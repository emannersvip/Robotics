#!/usr/bin/python3

# https://dev.pythonlibrary.org/2021/09/30/sqlite/
import sqlite3

# Local classes
from ehpc_datacenter import Datacenter
from ehpc_cluster import Cluster

if __name__ == '__main__':
    DC = Datacenter('PB')

    if DC.has_active_cluster():
        # Print ehpc CLI
        DC.print_ehpc_cli()
    else:
        # Walk user through setup process
        DC.setup_cluster()
