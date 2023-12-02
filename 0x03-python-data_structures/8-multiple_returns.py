#!/usr/bin/python3

def multiple_returns(sentence):
    """a function that returns a tuple with the length of a string
    and its first character.

    Args:
        sentence: the string

    Returns:
        a tuple with the length of sentence and its first character
        else None if sentence is empty.
    """
    length = len(sentence)
    first_char = sentence[0] if sentence else None
    return length, first_char
