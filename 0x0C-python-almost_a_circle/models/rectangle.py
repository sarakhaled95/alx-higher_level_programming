#!/usr/bin/python3
"""rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """method that returns the area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle in #"""
        rec = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rec, end="")

    def __str__(self):
        """string representative of rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.x, self.y,
                       self.width, self.height)

    def __update(self, id=None, width=None, height= None, x=None, y=None):
        """internal methode for update"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args):
        """updates arguments of rectangle"""
        if args:
            self.__update(*args)
