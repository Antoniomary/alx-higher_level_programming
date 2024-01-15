#!/usr/bin/python3
"""
    A module that defines the Rectangle class
"""
from .base import Base


class Rectangle(Base):
    """a class that defines a Rectangle. It is a subclass of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates a Rectangle class with private instance attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle instance with the character #
           it uses the the x value to print spaces before the rectangle
           while the y value to print new lines
        """
        print("\n" * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x, '#' * self.__width, sep='')

    def __str__(self):
        """returns the string representation of an instance in the format
           [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the fields of an instance.
           In *args:
            1st argument is the id attribute
            2nd argument is the width attribute
            3rd argument is the height attribute
            4th argument is the x attribute
            5th argument is the y attribute
           **kwargs does not mind.
           Uses **kwargs if *args is empty
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
                else:
                    break
        else:
            self.id = kwargs.get("id", self.id)
            self.__width = kwargs.get("width", self.__width)
            self.__height = kwargs.get("height", self.__height)
            self.__x = kwargs.get("x", self.__x)
            self.__y = kwargs.get("y", self.__y)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_repr = {
                "id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y
                }
        return dict_repr
