#!/usr/bin/python3

def no_c(my_string):
    """a function that removes all characters c and C from a string.

    Args:
        my_string: the original string to remove c and C

    Returns:
        the new string
    """
    if my_string:
        new_string = ""
        for char in my_string:
            if char not in "cC":
                new_string += char
        return new_string
