#!/usr/bin/python3
"""
This module is used to write in a file
"""


def write_file(filename="", text=""):
    """ write in a file """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
