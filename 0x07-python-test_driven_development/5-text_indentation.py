#!/usr/bin/python3
""" text_indentation module """


def text_indentation(text):
    """ prints a text with 2 new lines after ".?:"

    Args:
        text: the string text

    Raises:
        TypeError: if text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
