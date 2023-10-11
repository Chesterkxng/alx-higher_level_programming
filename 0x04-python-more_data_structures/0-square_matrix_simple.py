#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = []
    for sub_mtx in matrix:
        new_mtx.append(list(map(lambda x: x ** 2, sub_mtx)))
    return (new_mtx)
