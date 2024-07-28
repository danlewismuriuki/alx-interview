#!/usr/bin/python3

# 0-pascal_triangle.py
""" module 0-pascal_triangle.py """


def pascal_triangle(n):
    """
        Returns a list of list of intergers
        Args:
           n (int): size of the triangles
        Returns: list
    """

    if (n <= 0):
        return []

    res = [[1]]

    for i in range(n - 1):
        # prev_row is the last row in the res array conating the results
        prev_row = res[-1]
        # Example prev_row - len 2 nex_row - 3
        # Will fill the row with 1's example [1,1,1]
        next_row = [1] * (len(prev_row) + 1)

        # Add middle nums
        for j in range(1, len(prev_row)):
            next_row[j] = prev_row[j] + prev_row[j - 1]
        res.append(next_row)

    return res
