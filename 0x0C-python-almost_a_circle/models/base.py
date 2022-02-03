#!/usr/bin/python3
"""modulo base"""


class Base:
    """Class Base"""
    self.__nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = id
