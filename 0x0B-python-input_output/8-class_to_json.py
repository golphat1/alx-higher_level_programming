#!/usr/bin/python3
"""
Defines a Python class-to-JSON function.
obj is an instance of a Class
All attributes of the obj Class are serializable
Do not import any module
"""


def class_to_json(obj):
    """Return the dictionary represntation of simple data structure."""
    return obj.__dict__
