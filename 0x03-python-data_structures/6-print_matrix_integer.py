#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in (matrix):
        a = 0
        for j in (i):
            if a != 0:
                print(" ", end='')
            print("{:d}".format(j), end='')
            a += 1
        print()
