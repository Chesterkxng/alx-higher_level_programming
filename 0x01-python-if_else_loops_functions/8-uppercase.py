#!/usr/bin/python3
def uppercase(str):
    string = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            string += chr(ord(c) - 32)
        else:
            string += c
    print("{}".format(string))
