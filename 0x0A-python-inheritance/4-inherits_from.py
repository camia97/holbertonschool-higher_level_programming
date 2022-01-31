#!/usr/bin/python3
"""modulo"""


def inherits_from(obj, a_class):
    """function of inherits"""
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        return True
    else:
        return False