#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for x, y in a_dictionary.items():
        print(x, ': ', y)
