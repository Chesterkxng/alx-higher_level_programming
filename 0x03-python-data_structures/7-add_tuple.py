#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n, m = len(tuple_a), len(tuple_b)
    if n == 1:
        tuple_a = tuple_a[0], 0
    elif n == 0:
        tuple_a = 0, 0
    if m == 1:
        tuple_b = tuple_b[0], 0
    elif m == 0:
        tuple_b = 0, 0
    tuple_sum = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (tuple_sum)
