#!/usr/bin/python3
"""getting the area and perimeter of a rectangle"""


class Rectangle:
    """ Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialises instance data
        Args:
            width: width of the rectangle
            height: height of the rectangle
            Return: 0
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

        Rectangle.number_of_instances += 1

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

    def area(self):
        """prints the area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """prints the perimeter of a rectangle with an exception"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """String rep of rectangle class.
        prints a rectangle in form of hashtags
        to stdout.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle.append("#")
            until_last = self.__height - 1
            if x != until_last:
                rectangle.append("\n")
        return("".join(rectangle))

    def __repr__(self):
        """prints an oject"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
