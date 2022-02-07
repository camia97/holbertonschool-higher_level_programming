#!/usr/bin/python3
"""modulo tests base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test base"""
    def test_int(self):
        """test int"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(-4)
        self.assertEqual(c.id, -4)
        d = Base(87)
        self.assertEqual(d.id, 87)
