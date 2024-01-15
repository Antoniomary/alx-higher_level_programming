#!/usr/bin/python3
"""
    A module that defines the Square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """a class that defines a Square. It is a subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiates a Sqaure class with private instance attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation of an instance in the format
           [Square] (<id>) <x>/<y> - <size>
        """
        str_repr = super().__str__()
        str_repr.replace("Rectangle", "Square")
        end = str_repr.rfind('/')
        return str_repr[:end]

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the fields of an instance.
           In *args:
            1st argument is the id attribute
            2nd argument is the size attribute
            3th argument is the x attribute
            4th argument is the y attribute
           **kwargs does not mind.
           Uses **kwargs if *args is empty
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                else:
                    break
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("size", self.width)
            self.height = kwargs.get("size", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dict_repr = {
                "id": self.id, "size": self.width,
                "x": self.x, "y": self.y
                }
        return dict_repr
