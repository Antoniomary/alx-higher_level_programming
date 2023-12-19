#!/usr/bin/python3
"""a class definition named Square"""


class Square:
    """a class that defines a square by a private instance
    attribute: size. The size must be of type int and >= 0
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
