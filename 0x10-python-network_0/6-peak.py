#!/usr/bin/python3
"""module"""


def find_peak(list_of_integers):
    """function finde peak"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
