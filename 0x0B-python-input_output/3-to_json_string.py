#!/usr/bin/python3
"""
Function that returns JSON representation of an object(string).
No need to manage exceptions if the object can’t be serialized.
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
