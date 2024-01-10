#!/usr/bin/python3
"""
    A module for the Student class
"""


class Student:
    """defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """creates an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs:
            dict_rep = {}
            for attr in attrs:
                for key, value in self.__dict__.items():
                    if attr == key: 
                        dict_rep[key] = value
            return dict_rep
        else:
            return self.__dict__
