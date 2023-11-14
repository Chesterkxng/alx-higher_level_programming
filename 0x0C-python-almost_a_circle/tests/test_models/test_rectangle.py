#!/usr/bin/python3
"""
Unittest for the rectangle Class
"""


from models.rectangle import Rectangle
from models.base import Base
import unittest
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ testing rectangle """

    def test_instance(self):
        """ check if is instance or not """
        r = Rectangle(2, 4)
        self.assertIsInstance(r, Rectangle)

    def test_issubclass(self):
        """ check heritage """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_init_with_wrong_args(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(-1, 10)
        self.assertEqual(str(error.exception), "width must be > 0")

        with self.assertRaises(TypeError) as error:
            Rectangle("King", 10)
        self.assertEqual(str(error.exception), "width must be an integer")

        with self.assertRaises(TypeError) as error:
            Rectangle(10, "king")
        self.assertEqual(str(error.exception), "height must be an integer")

        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, "10")
        self.assertEqual(str(error.exception), "x must be an integer")

        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(error.exception), "y must be an integer")

        with self.assertRaises(ValueError) as error:
            Rectangle(0, 5)
        self.assertEqual(str(error.exception), "width must be > 0")

        with self.assertRaises(ValueError) as error:
            Rectangle(5, 0)
        self.assertEqual(str(error.exception), "height must be > 0")

        with self.assertRaises(ValueError) as error:
            Rectangle(5, 10, -1, 3)
        self.assertEqual(str(error.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as error:
            Rectangle(5, 10, 1, -3)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_update_1(self):
        """ test the update methode """
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(2, 2, 2, 2, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)

    def test_update_2(self):
        """ test update with kwargs """
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)

    def test_dict(self):
        dict_sample =  {
            "id": 1,
            "width": 2,
            "height": 2,
            "x": 0,
            "y": 0,
        }
        r1 = Rectangle(2, 2, 0, 0, 1)
        self.assertEqual(dict_sample, r1.to_dictionary())

    def test_savetofile(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_display(self):
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3)
            rect.display()
            result = output.getvalue()
            expected = ("##\n"
                        "##\n"
                        "##\n")
            self.assertEqual(result, expected)

    def test_display2(self):
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3, y=1)
            rect.display()
            result = output.getvalue()
            expected = ("\n"
                        "##\n"
                        "##\n"
                        "##\n")
            self.assertEqual(result, expected)

    def test_display3(self):
        with patch('sys.stdout', new_callable=StringIO) as output:
            rect = Rectangle(2, 3, x=1)
            rect.display()
            result = output.getvalue()
            expected = (" ##\n"
                        " ##\n"
                        " ##\n")
            self.assertEqual(result, expected)

    def test_loadfromfile(self):
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])
