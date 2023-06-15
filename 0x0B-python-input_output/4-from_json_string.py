#!/usr/bin/python3
"""
Defines a JSON-to-object function.
Don't manage exceptions if the JSON string doesn’t represent an object.
"""
import json


def from_json_string(my_str):
    """Return Python object representation of a JSON string."""
    return json.loads(my_str)
