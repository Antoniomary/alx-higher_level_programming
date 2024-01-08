#!/usr/bin/python3
"""
    A module for the ``inherits_from`` function
"""


def inherits_from(obj, a_class):
    """ returns True if an object is an instance of, or
        if the object is an instance of a class that inherited
        (directly or indirectly) from, a specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
