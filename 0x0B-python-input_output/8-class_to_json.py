#!/usr/bin/python3
"""
    A module for ``class_to_json`` function
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
       e.g (list, dictionary, string, integer and boolean)
       for JSON serialization of an object
    """
    return obj.__dict__
