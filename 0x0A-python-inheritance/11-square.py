#!/usr/bin/python3
"""module for square class"""
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

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
