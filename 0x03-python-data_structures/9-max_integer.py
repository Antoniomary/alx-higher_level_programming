#!/usr/bin/python3

def max_integer(my_list=[]):
    """a function that finds the biggest integer of a list.

    Args:
        my_list: the list

    Returns:
        the biggest integer in list else None if list is empty
    """
    if my_list:
        biggest = my_list[0]
        for num in my_list:
            if num > biggest:
                biggest = num
        return biggest
            
