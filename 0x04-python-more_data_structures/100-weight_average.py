#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    if not my_list:
        return (0)
    for tuplx in my_list:
        num += tuplx[0] * tuplx[1]
        den += tuplx[1]
    return (num/den)
