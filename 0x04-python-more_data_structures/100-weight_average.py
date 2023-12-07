#!/usr/bin/python3

def weight_average(my_list=[]):
    """a function that returns the weighted average of all integers
    tuple (<score>, <weight>)

    Args:
        my_list: the list

    Returns:
        the weighted average or 0 if list is empty
    """
    if not my_list:
        return 0

    average = 0
    divisor = 0
    for num in my_list:
        average += num[0] * num[1]
        divisor += num[1]

    return average / divisor
