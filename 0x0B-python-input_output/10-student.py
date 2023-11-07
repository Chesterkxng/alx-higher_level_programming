#!/usr/bin/python3
"""
Module that define a class of student
"""


class Student:
    """ class that definie a student """
    def __init__(self, first_name, last_name, age):
        """ initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ json repr """
        if attrs is None:
            return self.__dict__
        dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                dict[attr] = getattr(self, attr)
        return (dict)
