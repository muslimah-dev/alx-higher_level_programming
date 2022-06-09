#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_order = list(a_dictionary.keys())
    for i in new_order:
        print("{}: {}".format(i, new_order.get(i)))
