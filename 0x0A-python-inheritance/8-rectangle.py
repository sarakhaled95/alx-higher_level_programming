#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """a BaseGeometry class"""

    def area(self):
        """method to compute area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value

        args:
            name: name(string)
            value: integer

        raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle subclass"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
