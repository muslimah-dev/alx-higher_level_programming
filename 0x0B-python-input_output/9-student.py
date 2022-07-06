#!/usr/bin/python3
"""changes student class to JSON"""


class Student:
    """ student class with attributes first_name,
    last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """changes class to json"""
        return self.__dict__.copy()
