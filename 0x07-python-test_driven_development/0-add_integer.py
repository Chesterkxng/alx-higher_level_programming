#!/usr/bin/python3
"""
This module is used to add two integer
function(s):
           add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    function that used to return the sum of the value or raise TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
