#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """a function that prints all integers of a list, in reverse order.

    Args:
        my_list: the list to retrieve from.
    """
    if my_list:
        length = len(my_list)
        while length - 1 >= 0:
            print("{:d}".format(my_list[length - 1]))
            length -= 1
