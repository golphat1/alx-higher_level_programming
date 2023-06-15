#!/usr/bin/python3
"""
Function that defines a Pascal's Triangle function.
Do not import any module.
"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.
    Returns the list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
