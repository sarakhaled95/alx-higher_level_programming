#!/usr/bin/python3
"""addition module"""


def add_integer(a, b=98):
    """adds two integer and return the result


    Args:
        a: first integer
        b: second integer, default 98

    raises:
        TypeError: if a or b are not integers or float

    return:
        sum of both numbers
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/0-add_integer.txt")
