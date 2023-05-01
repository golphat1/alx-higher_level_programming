#!/usr/bin/python3
"""
Defines a file-writing function
Use the with statement.
No need to manage file permission exceptions
Function should create the file if doesn’t exist.
Function overwrite the content of the file if it already exists.
Don't allowed to import any module
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
