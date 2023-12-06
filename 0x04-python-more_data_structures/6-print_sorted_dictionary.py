#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys.

    Args:
        a_dictionary: the dictionary
    """
    if a_dictionary:
        for key in sorted(a_dictionary.keys()):
            print(key, a_dictionary[key], sep=": ")
