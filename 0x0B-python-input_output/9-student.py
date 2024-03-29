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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
