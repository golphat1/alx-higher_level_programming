#!/usr/bin/python3
# 0x0A. Python - Inheritance, task 0
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
