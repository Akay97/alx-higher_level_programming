#!/usr/bin/python3
"""
Unittests for the max_integer function.
"""

import unittest
from 6-main.py import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test with a list containing a single element
        self.assertEqual(max_integer([5]), 5)

        # Test with an empty list
        self.assertEqual(max_integer([]), None)

        # Test with a list of floats
        self.assertEqual(max_integer([1.5, 2.3, 3.8, 4.1]), 4.1)

        # Test with a list of mixed integers and floats
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)

        # Test with a list containing None
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

        # Test with a list of strings
        with self.assertRaises(TypeError):
            max_integer(["apple", "orange", "banana"])

if __name__ == '__main__':
    unittest.main()
