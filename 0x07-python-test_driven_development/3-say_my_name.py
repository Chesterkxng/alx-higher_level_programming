#!/usr/bin/python3
"""
This module is used to say a samne
"""


def say_my_name(first_name, last_name=""):
    """
    function that print the given name
    args:
    first_name (string):
                       the first name
    last_name (string):
                      the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
