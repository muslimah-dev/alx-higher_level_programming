#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ input checker  """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ input checker """
        return self.__width

    @property
    def height(self):
        """ input checker """
        return self.__height

    @property
    def x(self):
        """ input checker """
        return self.__x

    @property
    def y(self):
        """ input checker  """
        return self.__y

    @width.setter
    def width(self, value):
        """ input checker """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ input checker """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ input checker """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ input checker """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ input checker  """
        return self.__width * self.__height

    def display(self):
        """ input checker """
        print('\n' * self.__y + (" " * self.__x +
              (('#' * self.__width) + '\n')) * self.__height, end='')

    def __str__(self):
        """ input checker """
        str1 = ("[{}] ({:d}) {:d}/{:d} - {:d}".format
                (type(self).__name__, self.id, self.__x,
                 self.__y, self.__width))
        if type(self).__name__ == 'Rectangle':
            str1 = str1 + "/{:d}".format(self.__height)
        return str1

    def update(self, *args, **kwargs):
        """ input checker"""
        attrs = [self.id, self.__width, self.__height, self.__x, self.__y]
        var = ('id', 'width', 'height', 'x', 'y')
        if kwargs is not None and (args is None or len(args) is 0):
            for key, value in kwargs.items():
                if key in var:
                    attrs[var.index(key)] = value
            (self.id, self.__width, self.__height, self.__x, self.__y) = attrs
        else:
            args_aux = list(attrs[i] for i in range(len(args), 5))
            args_aux2 = list(args) + args_aux
            (self.id, self.__width, self.__height,
             self.__x, self.__y) = args_aux2

    def to_dictionary(self):
        """ input checker """
        new_dict = {'id': self.id,
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y}
        return new_dict
