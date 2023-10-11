#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    no_twins = []
    for c in set_1:
        if c not in set_2:
            no_twins.append(c)
    for c in set_2:
        if c not in set_1:
            no_twins.append(c)
    return (no_twins)
