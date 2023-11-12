#!/usr/bin/python3
"""
this module defines a Base class
"""
import json


class Base:
    """ A function that defines a Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Json string repr """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json repr to file """
        obj_lists = [obj.to_dictionary() for obj in list_objs]
        json_obj_lists = cls.to_json_string(obj_lists)
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(json_obj_lists)

    @staticmethod
    def from_json_string(json_string):
        """ return the list rep of json string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create an instnace with the dic """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return (inst)

    @classmethod
    def load_from_file(cls):
        """ load from a file """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                dicts = cls.from_json_string(f.read())
                lists = [cls.create(**dic) for dic in dicts]
                return (lists)
        except FileNotFoundError:
            return []
