#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    if n == 2:
        print("{} argument:".format(n - 1))
        print("{}: {}".format(n - 1, argv[n - 1]))
    if n > 2:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
