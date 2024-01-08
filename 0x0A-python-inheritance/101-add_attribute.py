#!/usr/bin/python3
"""
   A module that defines an ``add_attribute`` function
"""


def add_attribute(obj, name, value):
    """adds atttibute to an instance"""
    if hasattr(obj, "__dict__"):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
