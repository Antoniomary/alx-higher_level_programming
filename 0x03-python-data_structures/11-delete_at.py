#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """a function that deletes the item at a specific position in a list.

    Args:
        my_list: the list to delete from.
        idx: the index of the element to delete.

    Returns:
        the modified list else original list idx is negative or out of range.
    """
    if my_list:
        length = len(my_list)
        if 0 <= idx < length:
            del my_list[idx]
        return my_list
    return my_list
