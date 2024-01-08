#!/usr/bin/python3
"""
    A module for the ``is_kind_of_class`` function
"""


def is_kind_of_class(obj, a_class):
    """returns True if an object is an instance of, or
        if the object is an instance of a class that inherited from,
        a specified class; otherwise False
    """
    return isinstance(obj, a_class)
