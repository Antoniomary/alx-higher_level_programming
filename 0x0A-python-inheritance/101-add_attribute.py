#!/usr/bin/python3
"""
   A module that defines an ``add_attribute`` function
"""


def add_attribute(obj, name, value):
    """adds atttibute to an instance"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
        return
    elif hasattr(type(obj), "__slots__"):
        if name in type(obj).__slots__:
            obj.name = value
            return

    raise TypeError("can't add new attribute")
