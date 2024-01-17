#!/usr/bin/python3
"""This module read files and perform operation on it"""


def minOperations(n):
    """thsi function get the minimum number for a successful operation"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
