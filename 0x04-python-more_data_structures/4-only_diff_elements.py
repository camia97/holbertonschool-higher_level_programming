#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.copy()
    for i in set_1:
        for j in set_2:
            if i != j:
                set_3 = new_set.append(j)
    return set_3
