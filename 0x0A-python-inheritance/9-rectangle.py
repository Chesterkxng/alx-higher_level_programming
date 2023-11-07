#!/usr/bin/python3
"""
modules that define geometry base
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherit from Base Geometry
    """
    def __init__(self, width, height):
        """ initialize a rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ compute the aera of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ format the output """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
