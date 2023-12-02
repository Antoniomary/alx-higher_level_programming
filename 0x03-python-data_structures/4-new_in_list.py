#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """a function that replaces an element in a list at a specific
    position without modifying the original list

    Args:
        my_list: the list itself.
        idx: the index of the element to be replaced.
        element: the replacement.

    Returns:
        The modified list else the original list if:
        - idx is negative.
        - idx is out of range (> of number of element in my_list).
    """
    if my_list:
        new_list = my_list[:]
        length = len(new_list)
        if 0 <= idx < length:
            new_list[idx] = element
            return new_list
        return my_list
