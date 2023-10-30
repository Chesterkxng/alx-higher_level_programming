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
            area(self)
            perimeter(self)
            __str__(self)
            __repr__(self)
            __del__(self)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        rectangle init
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        compute the aera of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        compute the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return Rectangle string representation using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        representation = []
        for i in range(self.__height):
            representation.append("#" * self.__width)
        return "\n".join(representation)

    def __repr__(self):
        """ repr for eval """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ del for instance deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
