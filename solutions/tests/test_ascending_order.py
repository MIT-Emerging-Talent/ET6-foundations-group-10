#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contains the unit tests for the sort_numbers function."""

import unittest
from solutions.ascending_order_18.ascending_order import sort_numbers


class TestSortNumbers(unittest.TestCase):
    """tests for the sort_numbers function"""

    def test_empty_list(self):
        """Test if the function handles an empty list and returns an empty list."""
        self.assertEqual(sort_numbers([]), [])

    def test_sorted_list(self):
        """Test if the function returns the correct sorted list."""
        self.assertEqual(sort_numbers([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_negative_and_positive_numbers(self):
        """Test if the function handles negative and positive numbers correctly."""
        self.assertEqual(sort_numbers([5, -3, 9, -1, 0, 6]), [-3, -1, 0, 5, 6, 9])

    def test_large_numbers(self):
        """Test if the function handles large numbers correctly."""
        self.assertEqual(
            sort_numbers([200000, 500000, 1000000]), [200000, 500000, 1000000]
        )
