#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        for i in range(list_length):
            try:
                rest = my_list_1[i] / my_list_2[i]
                new_list.append(rest)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
                continue
            except (ValueError, TypeError):
                print("wrong type")
                new_list.append(0)
                continue
            except IndexError:
                print("out of range")
                new_list.append(0)
                continue
    finally:
        return (new_list)
