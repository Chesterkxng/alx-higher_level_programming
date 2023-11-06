#!/usr/bin/python3
"""
modules that define geometry base
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherit from Base Geometry
    """
    def __init__(self, width, height):
        """ initialize a rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
