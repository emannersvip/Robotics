#!/usr/bin/python3

class Datacenter:
    """EHPC class that defines a datacenter"""
    def __init__(self,name):
        # A datacenter is the base and global entity where all eHPC code resides.
        self.status = 'inactive'
        self.name   = name
        print("New datacenter %s created.", name)