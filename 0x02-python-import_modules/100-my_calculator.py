#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    num_of_args = len(argv)
    if num_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
