#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    result_list = []
    for x in range(0, list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (ValueError, TypeError,):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            result_list.append(res)
    return result_list
