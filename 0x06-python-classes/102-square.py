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
    area(self):
             return the value of the calculated area
    """
    def __init__(self, size=0):
        """
        Validate and Initialize the square instance with the size.
        Args
        ________
        size: int
             the size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """return the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        A function that modify the value of size
        Args
        _____
        value (int):
                 new value of size
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        a function returns the computed area of the square
        Return
        ------------
        int:
           area of the square
        """
        return (self.__size ** 2)

    def __eq___(self, other):
        """ equal """
        return self.size == other.size

    def __lt__(self, other):
        """ Less  than """
        return self.size < other.size

    def __le__(self, other):
        """ less equal than """
        return self.size <= other.size

    def __ne__(self, other):
        """ Non equal or different """
        return self.size != other.size

    def __ge__(self, other):
        """ great equal """
        return self.size >= other.size

    def __gt__(self, other):
        """ greater than """
        return self.size > other.size
