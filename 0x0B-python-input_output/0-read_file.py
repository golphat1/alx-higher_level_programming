#!/usr/bin/python3
"""
Defines a text file-reading function.
Must use the with statment.
You are not allowed to import any module.
You don’t need to manage file permission or file doesn't exist exceptions.
"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
