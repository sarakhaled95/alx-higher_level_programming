#!/usr/bin/python3
"""is same class module"""


def is_same_class(obj, a_class):
    """checks if the object is an instance of the specified 
    class

    args:
        obj: object
        a_class: specified class

    return:
        true or false
    """

    return type(obj) == a_class
