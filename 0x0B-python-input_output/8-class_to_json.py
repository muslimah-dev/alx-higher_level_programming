#!/usr/bin/python3
""" function thst returns the dictionary description with
simple data structure."""


def class_to_json(obj):
    """function that does the work
    Args:
        obj: instance of a class.
    Return: dictionary description with simple
    data structure
    """
    tem = {}
    if hasattr(obj, "__dict__"):
        tem = obj.__dict__.copy()
    return tem
