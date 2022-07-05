#!/usr/bin/python3
"""function that returns an object (Python d
ata
structure) represented by a JSON string"""


import json


def from_json_string(my_str):
    """
    Returns: object rep by a JSON string
    Args:
        my_str: string to be represented
    """
    json_object = json.loads(my_str)
    return json_object
