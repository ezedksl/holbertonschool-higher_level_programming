#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for x in new:
        if new.get(x):
            new[x] *= 2
    return new
