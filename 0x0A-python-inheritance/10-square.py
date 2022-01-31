#!/usr/bin/python3
"""modulo"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Rectangle"""
    def __init__(self, size):
        """define size"""
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)
