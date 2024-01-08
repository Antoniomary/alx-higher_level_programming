#!/usr/bin/python3
"""
   A module that defines an ``add_attribute`` function
"""


def add_attribute(obj, name, value):
    """adds atttibute to an instance"""
    if hasattr(obj, "__dict__"):
        obj.name = value
        return
    elif hasattr(obj, "__slots__"):
        attrs = getattr(obj, "__slots__", 0)
        for attr in attrs:
            if attr == name:
                obj.name = value
                return

    raise TypeError("can't add new attribute")
