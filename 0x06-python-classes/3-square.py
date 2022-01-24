#!/usr/bin/python3
""" Empty class """


class Square:
    """ Class Square"""
    def __init__(self, size=0):
        """Private instance attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method"""
        return self.__size * self.__size