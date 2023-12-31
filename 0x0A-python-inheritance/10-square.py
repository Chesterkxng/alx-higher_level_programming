#!/usr/bin/python3
"""
modules that define geometry base
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherit from rectangle
    """
    def __init__(self, size):
        """ initialize a square """
        self.integer_validator("square", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
            """ compute the aera of the rectangle """
            return (self.__size * self.__size)

        def __str__(self):
            """ format the output """
            return "[Rectangle] {}/{}".format(self.__size, self.__size)
