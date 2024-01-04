#!/usr/bin/python3
"""

    A shape module

"""


class Rectangle:
    """
        A class that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

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
        """prints the rectangle"""

        rect = ""

        if self.__height > 0 and self.__width > 0:
            b = self.__height
            while b > 0:
                rect += str(self.print_symbol) * self.__width
                b -= 1
                if b > 0:
                    rect += '\n'

        return rect

    def __repr__(self):
        """return a string representation of the existing rectangle"""
        return "Rectangle({:d},{:d})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an existing rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()

        if area_rect_1 >= area_rect_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """a class method that returns a new Rectangle instance
            with width == height == size
        """
        return cls(size, size)
