#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end=' ')
        print()
