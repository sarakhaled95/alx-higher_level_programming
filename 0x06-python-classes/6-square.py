#!/usr/bin/python3
"""square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0,0)):
        """construction

        args:
            size: length of one side of square
            position (int, int): the position of the new squares
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """set the current position of squares"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """prints the squares as #"""
        
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0,self.__position)]
            [print("#", end="") for k in range(self.size)]
            print("")
