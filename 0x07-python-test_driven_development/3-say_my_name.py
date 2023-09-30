#!/usr/bin/python3
""" say name module """


def say_my_name(first_name, last_name=""):
    """ function that prints first and last name


    args:
        first_name: first name
        last_name: holds the second name

    raises:
        TypeError: if first or last name is not string

    returns:
        nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
