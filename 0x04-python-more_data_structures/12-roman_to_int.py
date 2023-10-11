#!/usr/bin/python3
def roman_to_int(roman_string):
    key_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    conv_value = 0
    if not roman_string:
        return (None)
    for i in range(len(roman_string) - 1):
        if key_map[roman_string[i]] >= key_map[roman_string[i + 1]]:
            conv_value += key_map[roman_string[i]]
        else:
            conv_value -= key_map[roman_string[i]]
    conv_value += key_map[roman_string[len(roman_string) - 1]]
    return (conv_value)
