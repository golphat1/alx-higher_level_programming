#!/usr/bin/python3
# 0x0A. Python - Inheritance, task 0
"""Function that defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
