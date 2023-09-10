#!/usr/bin/python3

class Cluster:
    # A cluster only beconems active when it has a valid login node (role) and scheduler node (role).
    status      = 'inactive'