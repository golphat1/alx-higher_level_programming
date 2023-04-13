#!/usr/bin/python3
"""
Defines a Rectangle subclass Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialize the instance variables of Square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
