#!/usr/bin/python3
"""
A function that defines a file-appending function.
Create file if iy doesn't exist.
Must use the with statement
No need to manage file permission or file doesn't exist exceptions.
Do not import any module
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
