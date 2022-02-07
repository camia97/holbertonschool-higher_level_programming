#!/usr/bin/python3
"""modulo tests rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests rectangle"""
    def test_init(self):
        """test init"""
        a = Rectangle(4, 5, 0, 0, 1)
        self.assertEqual(a.width, 4)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 1)

    def tests_type(self):
        """tests type"""
        self.assertRaises(TypeError, Rectangle, 4, '5')
        self.assertRaises(TypeError, Rectangle, 3, 2, 'a')

    def tests_value(self):
        """tests value"""
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, -1 , 0)
        self.assertRaises(ValueError, Rectangle, 3, 4, -4, 7)
        self.assertRaises(ValueError, Rectangle, 2, 3, 7, -4)

    def test_area(self):
        """test area"""
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)

    def test_str(self):
        """test str"""
        r1 = (2, 4, 1, 3, 16)
        self.assertEqual(str(r1), "[Rectangle] (16) 1/3 - 2/4")
