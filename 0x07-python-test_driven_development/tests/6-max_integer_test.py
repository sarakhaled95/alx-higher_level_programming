#!/usr/bin/python3
""" Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test for max_integer([..])"""
    def test_no_arg(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([40]), 40)

    def test_unity(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([9, 9, 9]), 9)

    def test_max_start(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([9, 8, 7, 2]), 9)

    def test_max_end(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([2, 1, 4, 5]), 5)

    def test_ordered(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10]), 10)

    def test_unordered(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 1, 5]), 6)

    def test_pos_neg(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([-3000, -4667, 900, 923, 567, -999,
                                        888, 788]), 923)

    def test_negative(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([-333333, -555, -7999, -6000,
                                        -8999, -200]), -200)

    def test_ints_floats(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([10, 77.8, 100, 999.8, 9999]), 9999)

    def test_floats(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([11.3, 444.7, 600.999, 9.777,
                                    8.99]), 600.999)

    def test_numeric_string(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer("2987546"), "9")

    def test_lists(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([[], [3], [6], [7], [2, 9]]), [7])

    def test_str_list(self):
        """unit test for max_integer([..])"""
        self.assertEqual(max_integer([["cat"], ["boo"], ["bar"], ["foo"]
                                    ,["ric"]]), ["ric"])

    def test_inf(self):
        """Unit test for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)
