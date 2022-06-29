#!/usr/bin/python3
""" class Rectangle that defines a rectangle."""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialises instance data
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width tonew value"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height to new value"""
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
