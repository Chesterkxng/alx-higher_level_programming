#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5, 9, 10, 4]
idx = 7
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
