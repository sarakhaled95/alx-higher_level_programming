#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """determine if the object is an instance of a class that inherited
    from the specified class """

    return isinstance(obj, a_class) and type(obj) != a_class
