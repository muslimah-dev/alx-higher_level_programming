#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    try:
        length = 0
        new_list = my_list[:x]

        for x in new_list:
            length += 1
            print(x, end="")
        print()

    except SyntaxError as err:
        print("Syntax error")

    else:
        return length
