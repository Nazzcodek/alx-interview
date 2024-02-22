#!/usr/bin/python3
"""the 2d matrix rotation module"""


def rotate_2d_matrix(matrix):
    """this method rotate 2d matrix"""
    n = len(matrix[0])

    new_mat = [[None] * n for _ in range(n)]

    for col in range(n - 1, -1, -1):
        for row in range(0, n):
            new_mat[row][n - col - 1] = matrix[row][col]

            matrix[row].pop(0)

        matrix[row], new_mat[row] = new_mat[row], matrix[row]
