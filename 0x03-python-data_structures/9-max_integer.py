#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list_length = len(my_list)
    if my_list_length == 0:
        return (None)
    max_ = my_list[0]
    for i in range(1, my_list_length):
        if my_list[i] > max_:
            max_ = my_list[i]
    return (max_)
