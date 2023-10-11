#!/usr/bin/python3
def common_elements(set_1, set_2):
    twins = []
    for c in set_1:
        if c in set_2:
            twins.append(c)
    return (twins)
