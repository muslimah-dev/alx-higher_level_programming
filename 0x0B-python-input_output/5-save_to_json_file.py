#!/usr/bin/python3
"""function that writes an Object to a
text file, using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to text file
    Args:
        my_obj: Object.
        filename: name of textfile
    """
    with open(filename, 'w+') as fsave:
        json.dump(my_obj, fsave)
