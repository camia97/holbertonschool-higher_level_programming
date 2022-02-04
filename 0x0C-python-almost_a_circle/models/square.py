#!/usr/bin/python3
"""modulo Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """str method"""
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """property size"""
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = size
            self.height = size

    def update(self, *args, **kwargs):
        """Public method update"""
        dir_arg = {0:'id', 1:'size', 2:'x', 3:'y'}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, dir_arg[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """return dictionary"""
        my_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size, 
            'y': self.y
        }
        return my_dict
