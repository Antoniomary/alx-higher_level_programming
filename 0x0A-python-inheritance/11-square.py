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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return super().area()

    def __str__(self):
        """returns square description"""
        description = super().__str__()
        return description.replace("Rectangle", "Square")
