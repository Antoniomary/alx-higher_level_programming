#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integers.

    Args:
        matrix: a list containin a list.
    """
    if matrix:
        for r in matrix:
            col_l = len(r)
            if col_l == 0:
                print()
                return
            i = 0
            while i < col_l:
                print("{:d}".format(r[i]), end=" " if i + 1 < col_l else "\n")
                i += 1
