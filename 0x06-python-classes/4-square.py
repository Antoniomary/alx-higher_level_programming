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

    def area(self):
        """a public instance method that returns the area of square"""

        return self.__size ** 2

    @property
    def size(self):
        """it retrieves the value of the private attribute: size"""

        return self.__size

    @size.setter
    def size(self, value):
        """it sets the value of size"""
        if isinstance(value, int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
