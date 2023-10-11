#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    n = len(matrix)
    for i in range(n):
        sub_matrix = []
        for c in matrix[i]:
            sub_matrix.append(c ** 2)
        new_matrix.append(sub_matrix)
    return (new_matrix)
