#!/usr/bin/python3
"""
    A module for a look-up function
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
