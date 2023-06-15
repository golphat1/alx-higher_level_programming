#!/usr/bin/python3
"""
A function that defines a text file insertion function.
Use the with statement
No need to manage file permission or file doesn't exist exceptions.
Do not import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): Name of the file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as v:
        for line in v:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
