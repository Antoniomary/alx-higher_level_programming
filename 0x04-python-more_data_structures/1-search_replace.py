#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """a function that replaces all occurrences of an element by another
    in a new list.

    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

    Returns:
        the new_list with the replaced elements.
    """
    if list:
        new_list = []
        for element in my_list:
            new_list.append(replace if element == search else element)
        return new_list
