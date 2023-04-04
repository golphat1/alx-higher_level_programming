#!/usr/bin/python3
"""4-rectangle, Python project 0x08 task 4."""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        rows = ['#' * self.__width for _ in range(self.__height)]
        return '\n'.join(rows)

    def __str__(self):
        return self._draw_rectangle()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

