#!/usr/bin/python3
"""class module"""


class MyList(list):
    """costum MyList class"""
    def print_sorted(self):
        """ sort the list"""
        print(sorted(self))
