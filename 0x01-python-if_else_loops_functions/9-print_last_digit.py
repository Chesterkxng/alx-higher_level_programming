#!/usr/bin/python3
def print_last_digit(number):
    last_digit = repr(number)[-1]
    if last_digit:
        print("{}".format(last_digit), end='')
        return (int(last_digit))
