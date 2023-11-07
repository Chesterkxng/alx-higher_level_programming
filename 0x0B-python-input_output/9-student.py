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

    def to_json(self):
        """ json repr """
        return self.__dict__
