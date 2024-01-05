#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    i = None
    for num in list_of_integers:
        if i is None or i < num:
            i = num
    return i
