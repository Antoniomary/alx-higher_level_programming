#!/usr/bin/python3
"""
    A module to append text
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
       a specific string
    """
    if filename and search_string and new_string:
        with open(filename, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                file.write(line)
                if search_string in line:
                    file.write(new_string)
