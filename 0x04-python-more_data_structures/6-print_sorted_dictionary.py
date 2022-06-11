#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_order = list(a_dictionary.keys())
    new_order.sort()
    for i in new_order:
        print("{}: {}".format(i, a_dictionary.get(i)))
