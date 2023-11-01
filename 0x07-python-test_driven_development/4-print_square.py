#!/usr/bin/python3
"""
module used to print a square with given size
function(s):
           print_square(size)
"""


def print_square(size):
    """
    print the square based on his size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end='')
    elif size == 1:
        print("#")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print("")
