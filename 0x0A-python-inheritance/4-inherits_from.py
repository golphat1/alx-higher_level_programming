#!/usr/bin/python3
# 0x0A. Python - Inheritance, task 4
"""A function which checks if object is an instance of a class
that inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Return true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
