#!/usr/bin/python3
"""
    A module for matrix multipliacation
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """returns the multiplication of two matrices"""
    return numpy.matmul(m_a, m_b)
