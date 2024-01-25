#!/usr/bin/python3
"""
function that find a maximun in a list
"""
def find_peak(list_of_integers):
    """ max of a list """
    if not list_of_integers or len(list_of_integers) == 0:
        return None
    else:
        max_value = list_of_integers[0]
        for i in list_of_integers[1:]:
            if i > max_value:
                max_value = i
        return max_value
