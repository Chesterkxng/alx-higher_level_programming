#!/usr/bin/python3
"""
module that contains function
that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ load from a file """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.loads(f.readline()))
