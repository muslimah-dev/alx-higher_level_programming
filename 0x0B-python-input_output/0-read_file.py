#!/usr/bin/python3
"""function that reads a text file (UTF8)
and prints it to stdout"""

def read_file(filename=""):
    """ reads file and prints"""
    with open(filename) as f:
        """loop through via file handler"""
        for line in f:
            print(line)
