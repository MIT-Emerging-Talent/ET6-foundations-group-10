#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from solutions.check_odd_even import check_odd_even


class TestOddOrEven(unittest.TestCase):
    """Test the check_odd_even function"""

    def test_even_numbers(self):
        """Check if the number is even"""
        self.assertEqual(check_odd_even(2), "even_number")
        self.assertEqual(check_odd_even(8), "even_number")
        self.assertEqual(check_odd_even(1000000), "even_number")

    def test_odd_numbers(self):
        """Check if the number is odd"""
        self.assertEqual(check_odd_even(5), "odd_number")
        self.assertEqual(check_odd_even(1), "odd_number")
        self.assertEqual(check_odd_even(2000001), "odd_number")

    def test_edge_cases(self):
        """Check edge cases"""
        self.assertEqual(check_odd_even(0), "even_number")  # Zero is even
        self.assertEqual(check_odd_even(-1), "odd_number")  # Negative odd number
        self.assertEqual(check_odd_even(-2), "even_number")  # Negative even number


if __name__ == "__main__":
    unittest.main()
