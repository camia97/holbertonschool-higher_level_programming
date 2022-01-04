#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    for key, value in a_dictionary.items():
        if max_value < value:
            max_value = value
    return (key_list[val_list.index(max_value)])
