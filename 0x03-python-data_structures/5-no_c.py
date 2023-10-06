#!/usr/bin/python3
def no_c(my_string):
    my_string_cpy = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            my_string_cpy += c
    return (my_string_cpy)
