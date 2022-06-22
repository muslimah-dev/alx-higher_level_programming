#!/usr/bin/python3

""" class Square that defines a square by: Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)
You are not allowed to import any module
"""


class Square:
    """ Square class with a size and exceptions"""

    def __init__(self, size=0):
        """initializes a Square
        Args:
            size: size of square equal 0
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
