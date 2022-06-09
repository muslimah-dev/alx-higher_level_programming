#!/usr/bin/python3
def uniq_add(my_list=[]):
    ulist = set(my_list)
    result = 0
    for i in ulist:
        result += i
    return (result)
