#!/usr/bin/python3
"""
module that define function
function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """ a function that return Json representation of an object """
    return (json.dumps(my_obj))
