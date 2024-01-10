#!/usr/bin/python3
"""
    A file appender module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
       returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        bytes_added = f.write(text)

    return bytes_added
