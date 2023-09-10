#!/usr/bin/python3

class LoginNode:
    name    = 'login1'
    ip      = '192.168.100.1'
    idm     = 'local'  # Choose AD,LDAP,sssd, etc.
    storage = 'local'
    domain  = 'hpc.ehpc.org'        # I expect this to be set at the cluster level in the future.