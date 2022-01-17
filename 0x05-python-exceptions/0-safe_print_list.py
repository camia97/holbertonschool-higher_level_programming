#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pos = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            pos += 1
    except IndexError:
        pass
    print()
    return pos
