#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_array = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_array.append(key)
    for key in key_array:
        del a_dictionary[key]
    return (a_dictionary)
