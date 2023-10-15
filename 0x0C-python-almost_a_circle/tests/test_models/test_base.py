#!/usr/bin/python3
""" module for Base unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """tests for base class"""

    def setup(self):
        """
