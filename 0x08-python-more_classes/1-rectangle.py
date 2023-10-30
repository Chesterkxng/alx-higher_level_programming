#!/usr/bin/python3
"""
module to work with rectangles
"""


class Rectangle:
    """
    rectangle class
    attributes:
              width (int) : rectangle width
              height (int) :    ||    height
    methods:
            __init____
            getter and setter for attributes
    """
    def __init__(self, width=0, height=0):
        """
        rectangle init
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        return the height value
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        set the width value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        return the width value
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
