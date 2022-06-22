#!/usr/bin/python3
"""This is a Class Square thst defines a square"""

class Square:
    """square class"""
    def __init__(self, size=0):
        """Initializes a Square
        Args:
            size: size of the square
        """
        self.__size = size
    def size(self):
        """Getter method.
        Return:
            size
        """
        return self.__size
    def size(self, value):
        """Setter Method
        contains if / raise conditions.
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """ Finds the area of the square
        Returns:
            the area.
        """
        Area = self.__size * self.__size
        return Area
