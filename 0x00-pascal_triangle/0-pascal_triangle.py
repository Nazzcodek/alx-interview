#!/usr/bin/python3
"""
this module define pascal triangle of any number n
"""


def pascal_triangle(n):
    """This function return a pascal triagle of the nth argument"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
