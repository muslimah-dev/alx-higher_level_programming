#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns a list object
    Args:
        obj: object"""
    return dir(obj)
