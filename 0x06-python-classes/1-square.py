#!/usr/bin/python3
""" class Square that defines a square by Private instance attribute: size."""


class Square:
    """class Square with a private variable "size"."""
    def __init__(self, size):
        """Initializes a square.

        Args:
            size(int): size of Square
            """
        self.__size = size
