#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """a function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: the dictionary
        key: the key
        value: the value to attach to the key
    """
    a_dictionary[key] = value
    return a_dictionary
