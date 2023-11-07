#!/usr/bin/python3
"""
module to define int
"""


class MyInt(int):
    """
    class that inverse equality result test
    """
    def __eq__(self, other):
        """ invert the == op"""
        return super().__ne__(other)

    def __ne__(self, other):
        """invert the != op"""
        return super().__eq__(other)
