#!/usr/bin/python3

def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list: the list of integers.

    Returns:
        the sum of my_list.
    """
    if list:
        uniq_ints = set(my_list)
        return sum(uniq_ints)
