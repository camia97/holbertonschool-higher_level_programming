#!/usr/bin/python3
"""modulo"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""
        resu = {}
        if type(attrs) is list:
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
                if key in self.__dict__:
                    resu[key] = self.__dict__[key]
            return resu
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes"""
        json_dict = dict(json)
        for key in dict(self.__dict__):
            if key in json:
                self.__dict__[key] = json_dict[key]
