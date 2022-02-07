#!/usr/bin/python3
"""modulo base"""
import json
from os import path

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
        if list_dictionaries is None:
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
            return ([])
        if type(json_string) is not str:
            raise TypeError("jason_string must be an str")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new object"""
        if cls.__name__ == "Rectangle":
            c = cls(1, 2)
        elif cls.__name__ == "Square":
            c = cls(4)
        if c:
            c.update(**dictionary)
            return c

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_n = []
        name_file = f"{cls.__name__}.json"
        if path.isfile(f"{cls.__name__}.json"):
            with open(name_file, 'r') as f:
                for line in f:
                    try:
                        l_line = cls.from_json_string(line)
                        for i in l_line:
                            ins = cls.create(**i)
                            list_n.append(ins)
                    except Exception as a:
                        print(f"Error")
        return list_n
