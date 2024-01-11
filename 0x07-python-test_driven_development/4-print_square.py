#!/usr/bin/python3
"""
    A module that prints square shape
"""


def print_square(size):
    """prints a square with the character #"""
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for i in range(size)]
