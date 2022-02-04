#!/usr/bin/python3
"""modulo base"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json"""
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        list_n = []
        string = str(cls.__name__) + ".json"
        with open(string, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string(list_n))
            else:
                for ob in list_objs:
                    list_n.append(cls.to_dictionary(ob))
                f.write(cls.to_json_string(list_n))

    @staticmethod
    def from_json_string(json_string):
        """static method"""
        if json_string is None:
            return "[]"
        return json.dumps(json_string)
