#!/usr/bin/python3
"""
Unittest for the Square Class
"""


from models.square import Square
from models.rectangle import Rectangle
import unittest

class TestSquare(unittest.TestCase):
    """ testing rectangle """
    def test_instance(self):
        """ is instance ? """
        s1 = Square(4)
        self.assertIsInstance(s1, Square)

    def test_issubclass(self):
        """ is subclass ? """
        s1 = Square(5)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_area(self):
        """ test area """
        self.assertEqual(Square(3).area(), 9)

    def test_init_with_nv(self):
        """ width neg """
        with self.assertRaises(ValueError) as error:
            Square(-1)
        self.assertEqual(str(error.exception), "width must be > 0")

    def test_init_with_str(self):
        """ width str """
        with self.assertRaises(TypeError) as error:
            Square("King")
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_init_size_zero(self):
        """ width 0 """
        with self.assertRaises(ValueError) as error:
            Square(0)
        self.assertEqual(str(error.exception), "width must be > 0")

    def test_init_x_negative(self):
        """ x negative """
        with self.assertRaises(ValueError) as error:
            Square(5,-1, 3)
        self.assertEqual(str(error.exception), "x must be >= 0")

    def test_init_y_negative(self):
        """ y negative """
        with self.assertRaises(ValueError) as error:
            Square(5, 1, -3)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_size_setter(self):
        """ check the setter of size """
        s1 = Square(1)
        s1.size = 2
        self.assertEqual(s1.size, 2)

    def test_update_1(self):
        """ test update 1 """
        s1 = Square(7)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_update_2(self):
        """ test update 2 """
        s1 = Square(7)
        s1.update(size=4, id=2, y=3, x=4)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 3)

    def test_dict(self):
        dict_sample =  {
            "id": 1,
            "size": 2,
            "x": 0,
            "y": 0,
            }
        s1 = Square(2, 0, 0, 1)
        self.assertEqual(dict_sample, s1.to_dictionary())
