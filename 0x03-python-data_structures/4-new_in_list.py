#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_l = my_list[:] 
    if idx <= 0:
        n_l[idx] = element
    if idx > len(my_list):
        n_l[idx] = element
    return (n_l)
