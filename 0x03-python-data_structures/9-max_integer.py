#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for c in my_list:
            if c > max_int:
                max_int = c
        return (max_int)
