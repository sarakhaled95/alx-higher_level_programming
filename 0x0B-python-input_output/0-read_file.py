#!/usr/bin/python3
"""read file function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout

    args:
        filename: filename we need to read
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
