#!/usr/bin/python3
def print_last_digit(number):
        last_digit = repr(number)
        if isinstance(last_digit, int):
            print("{}".format(last_digit[-1]), end='')
            return (int(last_digit[-1]))
