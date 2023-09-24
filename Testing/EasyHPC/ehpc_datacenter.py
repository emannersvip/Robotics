#!/usr/bin/python3

# https://dev.pythonlibrary.org/2021/09/30/sqlite/
import sqlite3

class Datacenter:
    """EHPC class that defines a datacenter"""
    def __init__(self,name):
        # A datacenter is the base and global entity where all eHPC code resides.
        self.name   = name
        self.debug  = 1
        res = self.read_from_db('SELECT * FROM cluster')
        id, cluster_name, datacenter_name, has_login, has_scheduler, cluster_active = res
        if self.debug: print("Using Datacenter {}.".format(datacenter_name))
    
    def has_active_cluster(self):
        # This is a DB check.
        """A"""
        res = self.read_from_db('SELECT * FROM cluster')
        if len(res) >= 1:
            # A cluster exists. Now let's check iof it's active.
            id, cluster_name, datacenter_name, has_login, has_scheduler, cluster_active = res
            if cluster_active:
                print("Cluster {} is active!".format(cluster_name))
                return True
            else:
                print("Cluster {} exists but is not active.".format(cluster_name))
                if has_login == False:
                    print('-- Add a login node')
                if has_scheduler == False:
                    print('-- Add a scheduler node')
                return False
        else:
            # No active cluster
            return False

    def setup_cluster(self):
        """B"""
        print('No active cluster found. Beginnning setup procedure...')
        pass

    def print_ehpc_cli(self):
        """C"""
        pass

    def connect_to_db(self):
        """D"""
        # Initialize the environment
        ehpc_db_file = 'ehpc.db'
        sql_con = sqlite3.connect(ehpc_db_file)

        sql_cur = sql_con.cursor()
        return sql_cur
    
    # Returns SQL result from a read
    def read_from_db(self, sql):
        answer = ''
        sql_cur = self.connect_to_db()
        try:
            res = sql_cur.execute(sql)
            answer = res.fetchone()

            # Write proper check for valid data returned and handle appropriately
            # For now if tuple length is at least 1 we consider the sql result as valid output
            if len(answer) >= 1:
                if self.debug: print('Valid output returned.')
            else:
                if self.debug: print('Invalid output returned.')
        except Exception as e:
            print("Unhandled generic exception: {}".format(e))
        #finally:

        # Return appropriate return value (a tuple for now)
        return answer
