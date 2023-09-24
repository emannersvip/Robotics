#!/usr/bin/python3

class Cluster:
    """EHPC class that defines a cluster"""
    def __init__(self,name):
        # A cluster only beconems active when it has a valid login node (role) and scheduler node (role).
        self.status = 'inactive'
        self.name   = name
        print("New cluster %s created.", name)