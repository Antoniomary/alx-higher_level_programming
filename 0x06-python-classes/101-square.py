#!/usr/bin/python3
"""a class definition named Square"""


class Square:
    """a class that defines a square by a private instance
    attribute: size. The size must be of type int and >= 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (type(position[0]) == int and type(position[1]) == int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """prints to stdout the square with the character #
        if size is equal to 0, it print an empty line
        it prints spaces before the # character on a column if position is set
        """

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for line in range(self.__position[1]):
                    print()
            for row in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """it retrieves the value of the private attribute: position"""

        return self.__position

    @position.setter
    def position(self, value):
        """it sets the value of postion"""

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (type(position[0]) == int and type(position[1]) == int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __str__(self):
        """gives square printability"""

        diagram = ""
        if self.__position[1] > 0:
            for line in range(self.__position[1]):
                diagram += '\n'
        for row in range(self.__size):
            for space in range(self.__position[0]):
                diagram += ' '
            for col in range(self.__size):
                diagram += '#'
            diagram += '\n'
        return diagram[:-1]
