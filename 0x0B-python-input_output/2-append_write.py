#!/usr/bin/python3
"""
the module is used to append text in a file
"""


def append_write(filename="", text=""):
    """ append text in a file """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
