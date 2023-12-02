#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """a function that finds all multiples of 2 in a list.

    Args:
        my_list: the list

    Returns:
        a new list with True or False, depending on whether the integer
        at the same position in the original list is a multiple of 2.
    """
    if my_list:
        new_list = []
        for number in my_list:
            if number % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
