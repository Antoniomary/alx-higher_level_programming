#!/usr/bin/python3
"""
    A file reader module
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    if filename:
        with open(filename, encoding='utf-8') as f:
            print(f.read(), end='')
