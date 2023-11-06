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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
