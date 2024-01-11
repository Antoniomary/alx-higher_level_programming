#!/usr/bin/python3
"""
    An addition calculator module
"""


def add_integer(a, b=98):
    """an addition function that adds 2 integers"""
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
