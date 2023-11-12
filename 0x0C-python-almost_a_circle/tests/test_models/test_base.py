#!/usr/bin/python3
"""
unittest for Base class
"""


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ testing Base """
    def test_increment(self):
        """ test increment """
        self.assertEqual(Base(1).id, 1)
