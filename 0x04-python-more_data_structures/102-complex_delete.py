#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """a unction that deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: the dictionary
        value: the value to be deleted.

    Returns:
        modified dictionary
    """
    if a_dictionary:
        keys = list(a_dictionary.keys())
        for key in keys:
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary
