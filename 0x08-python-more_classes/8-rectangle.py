#!/usr/bin/python3
""" rectange class """


class Rectangle:
    """define a rectangle"""

    number_of_instances = 0
    """int: the number of active instance"""

    print_symbol = '#'
    """type: print symbol can be any type"""

    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method for area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method for perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        if self.__width != 0 and self.__height != 0:
            return ((str(self.print_symbol) * self.width + "\n") *
                    self.height)[:-1]

    def __repr__(self):
        """returns a string representation for production"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle

        Args:
            rect_1: first rectangle
            rect_2: second rectangle

        raises:
            TypeError: if rect_1 or rect_2 are not instance of Rectangle

        Return:
            the rectangle with the larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
