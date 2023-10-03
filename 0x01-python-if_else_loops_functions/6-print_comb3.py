#!/usr/bin/python3
for i in range(0, 10, 1):
    for j in range(i + 1, 10, 1):
        if (i != 8 or j != 9):
            print('{}'.format(i), end="")
            print('{}'.format(j), end=", ")
print("89")
