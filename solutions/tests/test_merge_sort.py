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

Created on 2024-01-06
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
