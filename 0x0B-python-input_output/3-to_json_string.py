#!/usr/bin/python3
"""
Defines a string-to-JSON function.
No need to manage exceptions if the object can’t be serialized.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
