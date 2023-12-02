#!/usr/bin/python3

def element_at(my_list, idx):
    """a function that retrieves an element from a list.

    Args:
        my_list: the list to retrieve from.
        idx: the index of the element to retrieve.

    Returns:
        The element at idx else None if:
        - idx is negative.
        - idx is out of range (> of number of element in my_list).
    """
    if my_list:
        length = len(my_list)
        if 0 <= idx < length:
            return my_list[idx]
