#!/usr/bin/python3
"""
    A module for a Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A class that defines a Rectangle shape, subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """creates an instance of Rectangle"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
