#!/usr/bin/python3
"""
    A file writer module
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
       returns the number of characters written:
    """
    with open(filename, 'w', encoding='utf-8') as f:
        bytes_written = f.write(text)

    return bytes_written
