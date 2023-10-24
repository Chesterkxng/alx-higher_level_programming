#!/usr/bin/python3
""" module that defines Square class
the Square Class represent a Square by his size
Classes:
       Square: A class manipulating squares objects
"""


class Square:
    """
    A class manipulating square object
    Attributes:
    __size: represent the size of the square
    Methods:
    __init__(self, size):
             initializing the square size
    """
    def __init__(self, size):
        """
        Initialize the square instance with the size.
        Args
        ________
        size: int
             the size of the square
        """
        self.__size = size
