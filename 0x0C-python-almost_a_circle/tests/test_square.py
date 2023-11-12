#!/usr/bin/python3
"""
Unittest for the Square Class
"""


from models.square import Square
import unittest

class TestSquare(unittest.TestCase):
    """ testing rectangle """
    def test_area(self):
        self.assertEqual(Square(3).area(), 9)

    def test_init_with_nv(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_init_with_str(self):
        with self.assertRaises(TypeError):
            Square("King")

    def test_init_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_init_x_negative(self):
        with self.assertRaises(ValueError):
            Square(5,-1, 3)

    def test_init_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 1, -3)
