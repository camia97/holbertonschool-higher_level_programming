#!/usr/bin/python3
def weight_average(my_list=[]):
    prom = 0
    add = 0
    for i in my_list:
        add = i[1] + add
        prom = (i[0] * i[1]) + prom
    return prom/add
