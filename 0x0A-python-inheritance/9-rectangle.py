#!/usr/bin/python3
"""module for rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle subclass"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """method which returns the area of rectangle"""

        return self.__width * self.__height
