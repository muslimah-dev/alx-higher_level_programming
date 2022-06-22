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

    @property
    def size(self):
        """Getter method.
        Return:
            size
        """
        return self.__size

    @size.setter
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
    def my_print(self):
        """Prints a square to stdout
        """
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("{}".format("#"), end='')
            print("{}".format("#"))
