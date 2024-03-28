#!/usr/bin/python3
"""a module for find peak function"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    nums = list_of_integers
    n = len(nums)
    mid = 0

    left, right = 0, n - 1
    while left <= right:
        mid = l + (r - l) // 2
        if ((mid == 0 or nums[mid - 1] <= nums[mid])
                and (mid == n - 1 or nums[mid] >= nums[mid + 1])):
            break
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return nums[mid]
