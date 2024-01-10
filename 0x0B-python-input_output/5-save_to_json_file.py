#!/usr/bin/python3
"""
    A module for saving serialized data
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    if my_obj and filename:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
