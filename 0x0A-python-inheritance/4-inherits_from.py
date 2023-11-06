#!/usr/bin/python3
"""
module to test the object classes
"""


def inherits_from(obj, a_class):
    """
    function that return true or false
    on classes comparassion
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
