#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function"""

    def test_empty(self):
        """tests result for empty list"""
        self.empty = max_integer()
        self.assertEqual(self.empty, None)
    
    def test_integers_max_end(self):
        """tests result for a list of integers when max is at end"""
        self.integers = max_integer([1, 2, 3, 4])
        self.assertEqual(self.integers, 4)

    def test_integers_max_beginning(self):
        """tests result for a list of integers when max is at beginning"""
        self.integers = max_integer([4, 3, 2, 1])
        self.assertEqual(self.integers, 4)

    def test_integers_max_middle(self):
        """tests result for a list of integers when max is at middle"""
        self.integers = max_integer([4, 3, 2, 1])
        self.assertEqual(self.integers, 4)


    def test_integers_with_negatives(self):
        """tests result when integers include negative number"""
        self.integers = max_integer([-4, 1, -8, 4])
        self.assertEqual(self.integers, 4)

    def test_negative_integers(self):
        """tests result when integers include negative number"""
        self.integers = max_integer([-4, -1, -8, -2])
        self.assertEqual(self.integers, -1)

    def test_list_with_one_element(self):
        """tests result when list has one element"""
        self.integers = max_integer([1])
        self.assertEqual(self.integers, 1)

    def test_non_lists(self):
        """tests that return value from func is an int"""
        self.type = max_integer((1, 2, 3, 4))
        self.assertEqual(isinstance(self.type, int), True)

if __name__ == "__main__":
    unittest.main()
