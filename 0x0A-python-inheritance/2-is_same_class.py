#!/usr/bin/python3
"""
    A module for the ``is_same_class`` function
"""


def is_same_class(obj, a_class):
    """returns True if an object is EXACTLY an instance of a specified class;
        otherwise False
    """
    return type(obj) == a_class
