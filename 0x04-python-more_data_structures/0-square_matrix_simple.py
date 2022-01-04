#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        a = map(lambda x: x * x, i)
        new_mat.append(list(a))
    return new_mat
