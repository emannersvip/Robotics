#!/usr/bin/python3

class SchedulerNode:
    """EHPC class that defines Scheduler(s)"""
    def __init__(self,name,scheduler):
        self.name        = name
        self.ip          = '192.168.99.1'
        self.scheduler   = scheduler   # Scheduler type ( SLURM, PBS, etc. used to point to install template)