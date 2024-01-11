#!/usr/bin/python3
"""

    A module for string formatting.

"""


def text_indentation(text):
    """prints 2 new lines after the characters: '.', '?' and ':' in a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # remove blanks at beginning and end of text
    new_text = text.strip(" \t")
    i = 0  # counter variable
    while i < len(new_text):
        print(new_text[i], end='')  # prints character at current index
        if new_text[i] in ".?:\n":  # characters that require formatting
            if not new_text[i] == '\n':
                print('\n')  # prints two new lines
            i += 1  # go to next index
            while i < len(new_text) and new_text[i] == '\n':
                print()
                i += 1

            if i < len(new_text):  # check for IndexError
                new_text = new_text[i:].lstrip(" \t")  # removes blanks
                i = 0  # start from 0 to account for len change in text
        else:
            i += 1
