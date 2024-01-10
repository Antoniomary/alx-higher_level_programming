#!/usr/bin/python3
"""
    A module for object creation for a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    if filename:
        with open(filename) as file:
            obj = json.load(file)

        return obj
