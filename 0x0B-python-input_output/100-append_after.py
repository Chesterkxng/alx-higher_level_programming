#!/usr/bin/python3
"""
module that append after
"""

def append_after(filename="", search_string="", new_string=""):
    """
    appends after
    """
    lines = []
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines[i:i + 1] = [lines[i], new_string]
            i += 1
        i += 1
    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(lines)
