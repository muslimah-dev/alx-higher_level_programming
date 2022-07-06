#!/usr/bin/puthon3
"""function that creates an object frim a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object
    Args:
        filenane: name of the file
    Returns: the fileobject created.
    """
    with open(filename, 'r') as f:
        return json.load(f)
