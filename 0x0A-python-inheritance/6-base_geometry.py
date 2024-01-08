#!/usr/bin/python3
"""
    A module that defines ``BaseGeometry`` class
"""


class BaseGeometry:
    """A class for doing geometry"""
    def __init__(self):
        """creates an instance"""
        pass

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
