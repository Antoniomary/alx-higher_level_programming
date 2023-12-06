#!/usr/bin/python3

def best_score(a_dictionary):
    """a function that returns a key with the biggest integer value.

    Args:
        a_dictionary: the dictionary

    Returns:
        the value that is biggest else None.
    """
    if a_dictionary:
        max_key = ""
        for key in a_dictionary:
            if not max_key:
                max_key = key
            elif a_dictionary[key] > a_dictionary[max_key]:
                max_key = key
        return max_key
