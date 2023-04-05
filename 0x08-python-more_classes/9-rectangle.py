#!/usr/bin/python3
"""9-rectangle, Python project 0x08 task 9."""

class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        return self._draw_rectangle()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1

    def _draw_rectangle(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = (f"{self.print_symbol}" * self.width + "\n") * (self.height - 1)
        rectangle += f"{self.print_symbol}" * self.width
        return rectangle

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle) or not isinstance(rect2, Rectangle):
            raise TypeError("Both arguments must be instances of Rectangle")
        return rect1 if rect1.area() >= rect2.area() else rect2

