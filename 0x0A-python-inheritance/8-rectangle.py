#!/usr/bin/python3
"""
modules that define geometry base
"""


class BaseGeometry:
    """
    improved geometry class
    """
    def area(self):
        """ raise execption """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validate the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

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
