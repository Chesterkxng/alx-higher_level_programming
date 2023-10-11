#!/usr/bin/python3
def uniq_add(my_list=[]):
    uq_list = []
    sum = 0
    for i in my_list:
        if i not in uq_list:
            uq_list.append(i)
            sum += i
    return (sum)
