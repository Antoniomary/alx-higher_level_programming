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

    def integer_validator(self, name, value):
        """validates value"""
        if not issubclass(int, type(value)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
