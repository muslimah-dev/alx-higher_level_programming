#!/usr/bin/python3
def no_c(my_string):
    l = 0
    new_s = my_string[:]
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_s = new_s[:(i - l)] + my_string[(i + 1):]
            l += 1
    return (new_s)
