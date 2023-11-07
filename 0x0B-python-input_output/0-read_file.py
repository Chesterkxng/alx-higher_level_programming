#!/usr/bin/python3
"""
module to open a file
"""


def read_file(filename=""):
    """ code to open file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
