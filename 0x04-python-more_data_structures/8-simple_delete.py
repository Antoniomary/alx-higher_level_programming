#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary.

    Args:
        a_dictionary: a dictionary
        key: the key

    Returns:
        modified dictionary
    """
    if a_dictionary:
        if key in a_dictionary.keys():
            del a_dictionary[key]
        return a_dictionary
