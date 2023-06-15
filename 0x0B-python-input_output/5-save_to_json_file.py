#!/usr/bin/python3
"""
iA function that defines a JSON file-writing function.
Use the with statement
No need to manage exceptions if the object can’t be serialized.
No need to manage file permission exceptions.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
