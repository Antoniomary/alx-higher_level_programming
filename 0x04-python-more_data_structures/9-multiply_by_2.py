#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """a function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: the dictionary

    Returns:
        a new dictionary
    """
    if a_dictionary:
        new_dictionary = {}
        for k, v in a_dictionary.items():
            new_dictionary[k] = v * 2
        return new_dictionary
