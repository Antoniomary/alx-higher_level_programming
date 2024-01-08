#!/usr/bin/python3
"""
    A module for a Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A class that defines a Square shape, subclass Rectangle
    """
    def __init__(self, size):
        """creates an instance of Square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return Rectangle.area(self)
