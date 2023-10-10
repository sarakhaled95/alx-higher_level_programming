#!/usr/bin/python3
""" student class module"""


class Student:
    """defines student"""

    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of student"""
        return self.__dict__
