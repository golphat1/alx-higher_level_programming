#!/usr/bin/python3
# 0x0A. Python - Inheritance, task 12
"""
MyInt class that inherits from int
and overrides the == and != operators
"""


class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
