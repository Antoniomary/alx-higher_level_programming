#!/usr/bin/python3
"""
    A module that defines ``MyInt`` class
"""


class MyInt(int):
    """A class that defines an int"""
    def __init__(self, number):
        """creates an instance"""
        super().__init__()
        self.number = number

    def __eq__(self, other):
        """returns True for False and False for True"""
        return False if int.__eq__(self, other) else True

    def __ne__(self, other):
        """returns True for False and False for True"""
        return False if int.__ne__(self, other) else True
