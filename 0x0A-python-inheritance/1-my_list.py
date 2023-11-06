#!/usr/bin/python3
"""
Module that inherit from list to
"""


class MyList(list):
    """
    class that inherit from list
    methods:
           print_sorted(self)
    """
    def print_sorted(self):
        """
        function that print the sorted list
        """
        print(sorted(self))
