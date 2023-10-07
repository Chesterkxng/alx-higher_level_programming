#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resp_list = []
    for c in my_list:
        if c % 2 == 0:
            resp_list.append(True)
        else:
            resp_list.append(False)
    return (resp_list)
