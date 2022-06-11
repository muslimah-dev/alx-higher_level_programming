#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = len(tuple_a)
    l_b = len(tuple_b)
    if l_a == 0:
        a1 = 0
        a2 = 0
    elif l_a == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    if l_b == 0:
        b1 = 0
        b2 = 0
    elif l_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    n_t = (a1 + b1), a2 + b2)
    return (n_t)
