#!/usr/bin/python3
"""Defines a class LockedClass with noobject or attribute."""


class LockedClass:
    """
    Prevent the user from instantiating/creating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
