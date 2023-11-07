#!/usr/bin/python3
"""
module that convert and save json rep in a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation """
    with open(filename, 'w', encoding="utf-8") as f:
        json_rep = json.dumps(my_obj)
        f.write(json_rep)
