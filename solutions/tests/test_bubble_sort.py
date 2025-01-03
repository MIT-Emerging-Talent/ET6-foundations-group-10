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

    def test_empty_list(self):
        """It should return [] for input []"""
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_one_element_list(self):
        """It should return [1] for input [1]"""
        actual = bubble_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_two_element_list(self):
        """It should return [1, 2] for input [2, 1]"""
        actual = bubble_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_three_elements_list(self):
        """It should return [1, 2, 3] for input [3, 2, 1]"""
        actual = bubble_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_four_elements_big_number_list(self):
        """It should return [1, 2, 3, 100500] for input [2, 3, 100500, 1]"""
        actual = bubble_sort([2, 3, 100500, 1])
        expected = [1, 2, 3, 100500]
        self.assertEqual(actual, expected)
