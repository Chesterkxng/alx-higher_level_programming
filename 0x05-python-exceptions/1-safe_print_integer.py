#!/usr/bin/python3
def safe_print_integer(value):
    try:
        num_value = int(value)
        print("{:d}".format(num_value))
        return (True)
    except:
        return (False)
