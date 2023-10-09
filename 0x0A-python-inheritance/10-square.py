#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """methode for square"""

    def __init__(self, size):
        """constractor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


    def area(self):
        return self.__size ** 2
