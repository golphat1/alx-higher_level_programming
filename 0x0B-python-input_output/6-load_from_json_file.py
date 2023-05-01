#!/usr/bin/python3
"""
Defines a JSON file-reading function.
Must use the with statement
No need to manage exceptions if the JSON string doesn’t represent an object.
No need to manage file permissions / exceptions.
"""
import json


def load_from_json_file(filename):
    """Create Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
