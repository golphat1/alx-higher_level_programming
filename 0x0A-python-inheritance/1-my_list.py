#!/usr/bin/python3
# 0x0A. Python - Inheritance, task 1

"""Function that defines an inherited list class MyList"""


class MyList(list):
    """A list type intended to only contain integers.
    """

    def print_sorted(self):
        """Print MyList lists in ascending order by value.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
