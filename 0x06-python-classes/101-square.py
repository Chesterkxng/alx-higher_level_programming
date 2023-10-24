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
    ------------

    __init__(self, size):
             initializing the square size

    area(self):
             return the value of the calculated area

    size(self):
             retrieve the value of size

    size(self, value):
            set the size with new value

    my_print(self):
            print a square with #
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Validate and Initialize the square instance with the size.
        Args
        ________
        size: int
             the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        a function returns the computed area of the square
        Return
        ------------
        int:
           area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ A function that print the square with # """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """ the print() """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                if i != self.__size - 1:
                    print("")
        print("")
