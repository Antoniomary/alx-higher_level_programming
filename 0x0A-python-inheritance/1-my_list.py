#!/usr/bin/python3
"""
    A module that defines a MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """creates an instance"""
        super().__init__(self)

    def print_sorted(self):
        """prints a list sorted in ascending order"""
        print(sorted(self))
