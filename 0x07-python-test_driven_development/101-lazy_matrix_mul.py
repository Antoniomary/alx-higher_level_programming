#!/usr/bin/python3
"""
    A module for matrix multipliacation
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """returns the multiplication of two matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for each in m_a:
        if not isinstance(each, list):
            raise TypeError("m_a must be a list of lists")
    for each in m_b:
        if not isinstance(each, list):
            raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for each in m_a:
        for element in each:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("m_a should contain only integers or floats")
    for each in m_b:
        for element in each:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_size_m_a = len(m_a[0])
    number_of_rows_m_a = 0
    for each in m_a:
        number_of_rows_m_a += 1
        if not len(each) == row_size_m_a:
            raise TypeError("each row of m_a must be of the same size")
    row_size_m_b = len(m_b[0])
    number_of_rows_m_b = 0
    for each in m_b:
        number_of_rows_m_b += 1
        if not len(each) == row_size_m_b:
            raise TypeError("each row of m_b must be of the same size")

    if not row_size_m_a == number_of_rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    return numpy.matmul(m_a, m_b)
