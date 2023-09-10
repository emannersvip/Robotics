#!/usr/bin/python3

class ComputeNode:
    """EHPC class that defines a Compute Node"""
    def __init__(self,name,queue):
        self.name    = name
        self.ip      = '192.168.200.1'
        self.queue   = 'cpu'

