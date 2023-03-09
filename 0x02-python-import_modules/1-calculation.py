#!/usr/bin/python3

if _name_ == "_main_":
    from calculator_1 import add, sub, mult, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b mult(a, b)))
    print("{} / {} = {}".format(a, b div(a, b)))
