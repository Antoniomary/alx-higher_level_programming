#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix.

    Args:
        matrix: is a 2 dimensional array.

    Returns:
        the new matrix with squared values of the old.
    """
    if matrix:
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append(list(map(lambda n: n * n, matrix[i])))
        return (new_matrix)
