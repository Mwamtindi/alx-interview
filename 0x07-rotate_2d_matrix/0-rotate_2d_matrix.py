#!/usr/bin/python3
"""
Rotate a n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate. Assumes non-empty.
    """
    n = len(matrix)
    # Transpose the matrix given
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each of the row
    for row in matrix:
        row.reverse()
