#!/usr/bin/python3
"""
unittest for Base class
"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """ testing Base """
    def test_increment(self):
        """ test increment """
        self.assertEqual(Base(1).id, 1)

    def test_instance(self):
        """ test instance """
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))

    def test_json_string(self):
        """ test to json string """
        r1 = Rectangle(10, 7, 2, 8, 1)
        desired_op = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, desired_op)

    def test_from_json(self):
        """ test from json to string """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        desired_op = [{"height": 4, "width": 10, "id": 89},
                       {"height": 7, "width": 1, "id": 7}]
        self.assertEqual(list_output, desired_op)

    def test_create(self):
        """ test create """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.id, 1)
