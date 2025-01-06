#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for merge_sort() function.

Test categories:
    - Standard cases: lists of type int with different lengths
    - Edge cases: empty lists, single element
    - Different data type: char, string, bool
    - Defensive tests:
        - side effects protection
        - input is not a collection
        - different data types in the input collection (non-homogeneous)

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""

import unittest

from ..merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    """Test the merge_sort function."""

    def test_1_empty_list(self):
        """It should return [] for input []"""
        actual = merge_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_2_one_int_element_list(self):
        """It should return [1] for input [1]"""
        actual = merge_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_3_two_int_elements_list(self):
        """It should return [1, 2] for input [2, 1]"""
        actual = merge_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_4_three_int_elements_list(self):
        """It should return [1, 2, 3] for input [3, 2, 1]"""
        actual = merge_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_5_four_int_elements_list_big_number(self):
        """It should return [1, 2, 3, 100500] for input [2, 3, 100500, 1]"""
        actual = merge_sort([2, 3, 100500, 1])
        expected = [1, 2, 3, 100500]
        self.assertEqual(actual, expected)
