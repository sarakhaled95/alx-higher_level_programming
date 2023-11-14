#!/usr/bin/python3
""" module for Base unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """tests for base class"""

    def setUp(self):
        """inmports module"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """cleans ufter each test"""
        pass

    def test_A_nb_objects_private(self):
        """tests if nb_objects is private class attribute"""
        self.assertTrur(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_private(self):
        """test if nb_objects initializes to zero"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

     def test_instantiation(self):
        """tests Base() instantiation."""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_constructor_args_2(self):
        """tests constructor signature with 2 notself args"""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_constructor(self):
        """tests constructor signature"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_consecutive_ids(self):
        """tests consecutive ids"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_synced(self):
        """tests sync between class and instance id"""
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_id_synced_more(self):
        """tests sync between class and instance id"""
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_id_int(self):
        """tests custom int id"""
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_custom_id_str(self):
        """tests custom int id"""
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_keyword(self):
        """tests id passed as keyword arg."""
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)
