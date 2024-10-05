#!/usr/bin/python3
"""
Module defining a fxn that returns a list of integer.
"""


def pascal_triangle(n):
    """Fxn pascal triangle to list the integer"""
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row as [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
