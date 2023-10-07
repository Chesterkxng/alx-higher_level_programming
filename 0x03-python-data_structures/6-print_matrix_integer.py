#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    p = len(matrix[0])
    if n != 0:
        for i in range(n):
            for j in range(p - 1):
                print("{}".format(matrix[i][j]), end=' ')
            print("{}".format(matrix[i][p - 1]))
    else:
        print()
