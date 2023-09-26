#!/usr/bin/python3
"""square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """construction

        args:
            size: length of one side of square
        """
        self.__size = size

    def area(self):
        """area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ property for the length of the side of this square

        raise:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints the squares as #"""
        for i in range(self.size):
            for k in range(self.size):
                print("#", end="\n" if k == self.size - 1 and i != k else "")
        print()
