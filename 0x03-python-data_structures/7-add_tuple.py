#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """a function that adds 2 tuples.

    Args:
        tuple_a = first tuple
        tuple_b = second tuple

    Returns:
        resulting tuple from addition.
    """
    if tuple_a and not tuple_b:
        return tuple_a
    elif tuple_b and not tuple_a:
        return tuple_a
    elif not tuple_a and not_tuple_b:
        return 0, 0
    else:
        len_a = len(tuple_a)
        len_b = len(tuple_b)

        x = tuple_a[0] + tuple_b[0]
        if len_a >= 2 and len_b >= 2:
            y = tuple_a[1] + tuple_b[1]
        elif len_a == 1 and len_b >= 2:
            y = tuple_b[1]
        elif len_b == 1 and len_a >= 2:
            y = tuple_a[1]

        tuple_c = x, y
        return tuple_c
