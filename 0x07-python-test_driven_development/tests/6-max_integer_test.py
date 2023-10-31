#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    testing class
    """
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 4, 6]), 6)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([6, 1, 2, 3]), 6)

    def test_max_at_the_middle(self):
        self.assertEqual(max_integer([1, 2, 10, 5, 6]), 10)

    def test_one_negative_value(self):
        self.assertEqual(max_integer([1, 4, -5, 10]), 10)

    def test_only_negative_value(self):
        self.assertEqual(max_integer([-2, -6, -1, -7]), -1)

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_no_element_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
