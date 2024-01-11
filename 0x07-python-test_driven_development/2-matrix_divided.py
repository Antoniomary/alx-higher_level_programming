#!/usr/bin/python3
"""
    module for division function
"""


def matrix_divided(matrix, div):
    """It divides all elements of a matrix"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(err_msg)

    for each_list in matrix:
        if not isinstance(each_list, list):
            raise TypeError(err_msg)

        for element in each_list:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError(err_msg)

    each_list_length = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) != each_list_length:
            raise TypeError(err_msg2)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for each in matrix:
        new = [n / div if n % div == 0 else round(n / div, 2) for n in each]
        new_matrix.append(new)

    return new_matrix
