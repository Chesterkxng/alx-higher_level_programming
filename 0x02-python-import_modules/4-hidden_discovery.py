#!/usr/bin/python3.8
import hidden_4
if __name__ == "__main__":
    vars = dir(hidden_4)
    for var in sorted(vars):
        if not var.startswith('__'):
            print("{}".format(var))
