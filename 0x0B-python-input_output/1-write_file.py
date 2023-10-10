#!/usr/bin/python3
"""write function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    Return:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
