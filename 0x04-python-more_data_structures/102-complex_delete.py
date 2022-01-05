#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = []
    for keys, v in a_dictionary.items():
        if (v == value):
            k.append(keys)
    for i in k:
        del a_dictionary[i]
    return a_dictionary
