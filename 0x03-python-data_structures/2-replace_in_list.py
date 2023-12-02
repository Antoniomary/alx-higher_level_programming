#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """a function that replaces an element of a list at a specific position.

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
        length = len(my_list)
        if 0 <= idx < length:
            my_list[idx] = element
        return my_list
