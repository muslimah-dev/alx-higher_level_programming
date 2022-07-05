#!/usr/bin/python3
"""function that appends a string at the
end of a text file (UTF8) and returns
the number of characters added"""


def append_write(filename="", text=""):
    """returns number of characters appended
    Args:
        filename: name of the file
        text: set of chars appended
    """
    with open(filename, 'a') as fout:
        return fout.write(text)
