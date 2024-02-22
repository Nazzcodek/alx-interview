#!/usr/bin/python3
"""the 2d matrix rotation module"""


def rotate_2d_matrix(matrix):
    """This method rotates a  2D matrix  90 degrees clockwise in place."""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
