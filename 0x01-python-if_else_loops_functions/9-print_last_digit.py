#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        last_digit = repr(number)[-1]
        print("{}".format(last_digit), end='')
        return (int(last_digit))
