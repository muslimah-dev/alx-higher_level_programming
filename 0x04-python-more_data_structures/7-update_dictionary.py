#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update = a_dictionary.keys()
    values = a_dictionary.values()
    a_dictionary[key] = value
    print("{}: {}".format(update, values)
