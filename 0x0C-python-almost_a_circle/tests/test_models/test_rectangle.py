#!/usr/bin/python3
"""
Unittest for the rectangle Class
"""


from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    """ testing rectangle """
    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_init_with_nv(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 10)

    def test_init_with_str(self):
        with self.assertRaises(TypeError):
            Rectangle("King", 10)

    def test_init_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_init_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_init_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 3)

    def test_init_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -3)
