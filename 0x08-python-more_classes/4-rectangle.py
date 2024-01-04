#!/usr/bin/python3
"""

    A shape module

"""


class Rectangle:
    """
        A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """creates the instances of rectangle class"""
        if type(width) is int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) is int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a Rectangle instance"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """retrieves the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a Rectangle instance"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle using '#'"""
        rect = ""

        if self.__height > 0 and self.__width > 0:
            b = self.__height
            while b > 0:
                w = self.__width
                while w > 0:
                    rect += '#'
                    w -= 1
                b -= 1
                if b > 0:
                    rect += '\n'

        return rect

    def __repr__(self):
        """return a string representation of the existing rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
