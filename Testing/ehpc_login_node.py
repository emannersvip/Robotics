#!/usr/bin/python3

class LoginNode:
    """EHPC class that defines Login Nodes"""
    def __init__(self, name, ip):
        self.name    = name
        self.ip      = '192.168.100.1'
        self.idm     = 'local'  # Choose AD,LDAP,sssd, etc.
        self.storage = 'local'
        self.domain  = 'hpc.ehpc.org'        # I expect this to be set at the cluster level in the future.