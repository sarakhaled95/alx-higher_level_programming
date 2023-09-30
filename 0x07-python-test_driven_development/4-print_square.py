#!/usr/bin/python3
""" print_squale methode module"""


def print_square(size):
    """ method that prints a square with the character #

    args:
        size: rows and coloumns in hashes

    raises:
        TypeError: if size is not integer
        ValueError: if size is less than 0

    return:
        nothing
    """

    if size < 0:
        raise ValueError("size must be >= 0")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
        
    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
