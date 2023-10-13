#!/usr/bin/python3
"""square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__,
                self.id , self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
