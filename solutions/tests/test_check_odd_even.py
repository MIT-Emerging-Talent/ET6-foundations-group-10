#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains the tests for the check_odd_even function."""

import unittest
from solutions.check_odd_even_17.check_odd_even import check_odd_even


class TestOddOrEven(unittest.TestCase):
    """Test cases for the check_odd_or_even function."""

    def test_even_numbers(self):
        """the test for even numbers"""
        self.assertEqual(check_odd_even(2), "even_number")
        self.assertEqual(check_odd_even(1000000), "even_number")
        self.assertEqual(check_odd_even(0), "even_number")

    def test_odd_numbers(self):
        """the test for odd numbers"""
        self.assertEqual(check_odd_even(5), "odd_number")
        self.assertEqual(check_odd_even(500001), "odd_number")
        self.assertEqual(check_odd_even(-1), "odd_number")

    def test_edge_cases(self):
        """with edge cases"""
        self.assertEqual(check_odd_even(0), "even_number")
        self.assertEqual(check_odd_even(1), "odd_number")
        self.assertEqual(check_odd_even(-1), "odd_number")

    def test_large_integers(self):
        """the test for large integers"""
        self.assertEqual(check_odd_even(200000), "even_number")
        self.assertEqual(check_odd_even(500000), "even_number")
        self.assertEqual(check_odd_even(1000000), "even_number")
