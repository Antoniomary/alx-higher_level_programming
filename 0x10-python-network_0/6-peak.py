#!/usr/bin/python3
"""a module for find peak function"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    nums = list_of_integers
    n = len(nums)

    if n == 1:
        return nums[0]
    elif n == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    else:
        for i in range(1, n - 1):
            if i - 1 == 0 and nums[0] > nums[1]:
                return nums[i - 1]
            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return nums[i]
        return nums[-1] if nums[-1] > nums[-2] else nums[-2]
