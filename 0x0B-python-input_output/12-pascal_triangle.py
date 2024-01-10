#!/usr/bin/python3
"""
    A module for a ``pascal_triangle`` function
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
       the Pascal’s triangle of n
    """
    triang = []

    if n == 1:
        triang = [[1]]
    elif n >= 2:
        triang = [[1], [1, 1]]
        if n > 2:
            for row in range(2, n):
                res = [1]
                for col in range(1, row):
                    res.append(triang[row - 1][col - 1] + triang[row - 1][col])
                res += [1]
                triang.append(res)

    return triang
