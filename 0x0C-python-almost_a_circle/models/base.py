#!/usr/bin/python3
"""
this module defines a Base class
"""


class Base:
    """ A function that defines a Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects
