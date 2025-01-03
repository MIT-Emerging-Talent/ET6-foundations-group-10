#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for bubble_sort function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single element
    - Defensive tests: wrong input types, different input types

Created on 2024-01-03
Author: Oleksandr Maksymikhin
"""

import unittest

from ..bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test the bubble_sort function."""

    # Uncomment for predictive stepping
    # actual_1 = bubble_sort([])
    # actual_2 = bubble_sort([1])
    # actual_3 = bubble_sort([2, 1])
    # actual_4 = bubble_sort([3, 2, 1])
    # actual_5 = bubble_sort([2, 3, 100500, 1])
    # actual_6 = bubble_sort(["b", "a", "c"])
    # actual_7 = bubble_sort(["cabbage", "banana", "apple"])
    # actual_8 = bubble_sort([True, False, True, False])

    def test_empty_list(self):
        """It should return [] for input []"""
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_one_int_element_list(self):
        """It should return [1] for input [1]"""
        actual = bubble_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_two_int_element_list(self):
        """It should return [1, 2] for input [2, 1]"""
        actual = bubble_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_three_int_elements_list(self):
        """It should return [1, 2, 3] for input [3, 2, 1]"""
        actual = bubble_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_four_int_elements_big_number_list(self):
        """It should return [1, 2, 3, 100500] for input [2, 3, 100500, 1]"""
        actual = bubble_sort([2, 3, 100500, 1])
        expected = [1, 2, 3, 100500]
        self.assertEqual(actual, expected)

    def test_chars_list(self):
        """It should return ["a", "b", "c"] for input ["b", "a", "c"]"""
        actual = bubble_sort(["b", "a", "c"])
        expected = ["a", "b", "c"]
        self.assertEqual(actual, expected)

    def test_string_list(self):
        """It should return ["apple", "banana", "cabbage"] for input ["cabbage", "banana", "apple"]"""
        actual = bubble_sort(["cabbage", "banana", "apple"])
        expected = ["apple", "banana", "cabbage"]
        self.assertEqual(actual, expected)

    def test_bool_list(self):
        """It should return [False, False, True, True] for input [True, False, True, False]"""
        actual = bubble_sort([True, False, True, False])
        expected = [False, False, True, True]
        self.assertEqual(actual, expected)
