#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """a function that prints all integers of a list.

    Args:
        my_list: a list of the integers to print.
    """
    for number in my_list:
        print("{:d}".format(number))
