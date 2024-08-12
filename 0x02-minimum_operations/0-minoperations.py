#!/usr/bin/python3
"""
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n <= 1:
        return 0

    operations = 0
    division = 2

    while n > 1:
        if n % division == 0:
            while n % division == 0:
                n //= division
                operations += division
        division += 1

    return operations
