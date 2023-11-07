#!/usr/bin/python3
"""
Module that add all arguments in a python list
"""

import sys


if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        list_ = load_from_json_file("add_item.json")
    except:
        list_ = []
    for element in sys.argv[1:]:
        list_.append(element)
    save_to_json_file(list_, "add_item.json")
