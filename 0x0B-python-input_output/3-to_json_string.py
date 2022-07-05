#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """returns object to JSon
    Args:
        my_obj: object to turn.
    """
    json_object = json.dumps(my_obj)
    return(json_object)
