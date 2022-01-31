#!/usr/bin/python3
"""modulo"""


class BaseGeometry:
    """Class base geometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        