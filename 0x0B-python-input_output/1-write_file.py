#!/usr/bin/python3
"""function that writes a string to a text file
(UTF8) and returns the number of characters
written"""


def write_file(filename="", text=""):
    """prototype
    """
    with open(filename, 'w+') as fout:
        return(fout.write(text))
