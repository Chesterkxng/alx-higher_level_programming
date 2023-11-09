#!/usr/bin/python3
"""
this module defines Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validator(self, name, value):
        """ function that validate the inout """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return (value)

    @property
    def width(self):
        """ retrieve the width """
        return (self.__width)

    @width.setter
    def width(self, width):
        """ set the width """
        self.__width = self.validator("width", width)

    @property
    def height(self):
        """ retrieve the height """
        return (self.__height)

    @height.setter
    def height(self, height):
        """ set the height """
        self.__height = self.validator("height", height)

    @property
    def x(self):
        """ retrieve x """
        return (self.__x)

    @x.setter
    def x(self, x):
        """ set x """
        self.__x =  self.validator("x", x)

    @property
    def y(self):
        """ retrieve y """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ set y """
        self.__y = self.validator("y", y)
