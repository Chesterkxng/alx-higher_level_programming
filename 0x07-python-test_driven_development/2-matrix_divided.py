#!/usr/bin/python3
"""
This module is used to divided a matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    divide a matrix by a div and return a new matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    n = len(matrix[0])
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for submatrix in matrix:
        if len(submatrix) != n:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in submatrix:
            if not isinstance(elem, (float, int)):
                raise TypeError(err_msg)
    new_matrix = []
    for submatrix in matrix:
        sub_matrix = []
        for elem in submatrix:
            sub_matrix.append(round((elem / div), 2))
        new_matrix.append(sub_matrix)
    return (new_matrix)
