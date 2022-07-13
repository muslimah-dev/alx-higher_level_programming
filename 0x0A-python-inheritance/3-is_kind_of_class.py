#!/usr/bin/python3
"""Module check class and subclass
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class class
    Args:
        obj: object of the class
        a_class: class
    return: true if object is an instance of a class that inherited from"""
    return isinstance(obj, a_class)
