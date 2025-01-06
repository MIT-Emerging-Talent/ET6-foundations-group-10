#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for merge_sort() function.

Test categories:
    - Standard cases: lists of type int with different lengths
    - Edge cases: single element
    - Different data type: string, bool
    - Defensive tests:
        - side effects protection
        - input is not a collection
        - input of empty collection
        - different data types in the input collection (non-homogeneous)
        - input data types are not processed by module

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""

import unittest

from ..merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    """Test the merge_sort function."""

    def test_1_one_int_element_list(self):
        """It should return [1] for input [1]"""
        actual = merge_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_2_two_int_elements_list(self):
        """It should return [1, 2] for input [2, 1]"""
        actual = merge_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_3_three_int_elements_list(self):
        """It should return [1, 2, 3] for input [3, 2, 1]"""
        actual = merge_sort([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_4_four_int_elements_list_big_number(self):
        """It should return [1, 2, 3, 100500] for input [2, 3, 100500, 1]"""
        actual = merge_sort([2, 3, 100500, 1])
        expected = [1, 2, 3, 100500]
        self.assertEqual(actual, expected)

    def test_5_char_elements_list(self):
        """It should return ["a", "b", "c", "d"] for input ["b", "d", "a", "c"]"""
        actual = merge_sort(["b", "d", "a", "c"])
        expected = ["a", "b", "c", "d"]
        self.assertEqual(actual, expected)

    def test_6_string_elements_list(self):
        """It should return ["apple", "banana", "cabbage", "daikon"] for input ["daikon", "cabbage", "banana", "apple"]"""
        actual = merge_sort(["daikon", "cabbage", "banana", "apple"])
        expected = ["apple", "banana", "cabbage", "daikon"]
        self.assertEqual(actual, expected)

    def test_7_bool_elements_list(self):
        """It should return [False, False, True, True] for input [True, False, False, True]"""
        actual = merge_sort([True, False, False, True])
        expected = [False, False, True, True]
        self.assertEqual(actual, expected)

    def test_8_side_effect_protection(self):
        """It should return [3, 2, 1] of initial input"""
        input_list = [3, 2, 1, 100500]
        copy_for_sorting = input_list.copy()
        merge_sort(copy_for_sorting)
        self.assertEqual(input_list, [3, 2, 1, 100500])

    def test_9_non_collection_input(self):
        """It should raise an assertion error if the input is not a collection"""
        with self.assertRaises(AssertionError):
            merge_sort("banana")

    def test_10_non_homogeneous_collection_input(self):
        """It should raise an assertion error if the collection is non-homogeneous"""
        with self.assertRaises(AssertionError):
            merge_sort([3, 2, "one"])

    def test_11_input_of_empty_collection(self):
        """It should raise an assertion error if the input data type is out of processed type"""
        with self.assertRaises(AssertionError):
            merge_sort([])

    def test_12_input_of_non_processed_data_type(self):
        """It should raise an assertion error if the input data type is out of processed type"""
        with self.assertRaises(AssertionError):
            merge_sort([{1, "one"}, {2, "two"}])
