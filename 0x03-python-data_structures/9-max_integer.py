#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    a = None
    for i in my_list:
        if (a is None or i > a):
            a = i
    return a
