#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for bubble_sort() function.

Test categories:
    - Standard cases: lists of type int with different lengths
    - Edge cases: empty lists, single element
    - Different data types: char, string, bool
    - Defensive tests:
        - side effects protection
        - input is not a collection
        - different data types in the input collection (non-homogeneous)

Created on 2024-01-03
Author: Oleksandr Maksymikhin
"""

import unittest

from ..bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test the bubble_sort function."""

    def test_1_empty_list(self):
        """It should return [] for input []"""
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_2_one_int_element_list(self):
        """It should return [1] for input [1]"""
        actual = bubble_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_3_two_int_elements_list(self):
        """It should return [1, 2] for input [2, 1]"""
        actual = bubble_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_4_three_int_elements_list(self):
        """It should return [1, 2, 3] for input [3, 2, 1]"""
        actual = bubble_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_5_four_int_elements_list_big_number(self):
        """It should return [1, 2, 3, 100500] for input [2, 3, 100500, 1]"""
        actual = bubble_sort([2, 3, 100500, 1])
        expected = [1, 2, 3, 100500]
        self.assertEqual(actual, expected)

    def test_6_char_elements_list(self):
        """It should return ["a", "b", "c"] for input ["b", "a", "c"]"""
        actual = bubble_sort(["b", "a", "c"])
        expected = ["a", "b", "c"]
        self.assertEqual(actual, expected)

    def test_7_string_elements_list(self):
        """It should return ["apple", "banana", "cabbage"] for input ["cabbage", "banana", "apple"]"""
        actual = bubble_sort(["cabbage", "banana", "apple"])
        expected = ["apple", "banana", "cabbage"]
        self.assertEqual(actual, expected)

    def test_8_bool_elements_list(self):
        """It should return [False, False, True, True] for input [True, False, True, False]"""
        actual = bubble_sort([True, False, True, False])
        expected = [False, False, True, True]
        self.assertEqual(actual, expected)

    def test_9_side_effect_protection(self):
        """It should return [3, 2, 1] of initial input"""
        input_list = [3, 2, 1]
        bubble_sort(input_list)
        self.assertEqual(input_list, [3, 2, 1])

    def test_10_non_collection_input(self):
        """It should raise an assertion error if the input is not a collection"""
        with self.assertRaises(AssertionError):
            bubble_sort("apple")

    def test_11_non_homogeneous_collection_input(self):
        """It should raise an assertion error if the collection is non-homogeneous"""
        with self.assertRaises(AssertionError):
            bubble_sort([3, "two", 1])
