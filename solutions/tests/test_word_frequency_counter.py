#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 01.01.2025

@author: Ahmad Hamed Dehzad
"""

import unittest

from solutions.word_frequency_counter import word_frequency_counter


class TestWordFrequencyCounter(unittest.TestCase):
    """Test the word_frequency_counter function"""

    def test_empty_string(self):
        """It should evaluate an empty string to an empty dictionary"""
        actual = word_frequency_counter("")
        expected = {}
        self.assertEqual(actual, expected)

    def test_single_word(self):
        """It should evaluate a single word correctly"""
        actual = word_frequency_counter("Hello")
        expected = {"hello": 1}
        self.assertEqual(actual, expected)

    def test_multiple_words(self):
        """It should count the frequency of multiple words"""
        actual = word_frequency_counter("Hello world hello")
        expected = {"hello": 2, "world": 1}
        self.assertEqual(actual, expected)

    def test_case_insensitivity(self):
        """It should treat words case-insensitively"""
        actual = word_frequency_counter("Apple apple APPLE")
        expected = {"apple": 3}
        self.assertEqual(actual, expected)

    def test_with_punctuation(self):
        """It should handle words with punctuation correctly"""
        actual = word_frequency_counter("Hello, world! Hello.")
        expected = {"hello,": 1, "world!": 1, "hello.": 1}
        self.assertEqual(actual, expected)

    def test_numbers_in_string(self):
        """It should handle strings with numbers"""
        actual = word_frequency_counter("123 123 456")
        expected = {"123": 2, "456": 1}
        self.assertEqual(actual, expected)

    def test_non_string_input(self):
        """It should raise a ValueError if the input is not a string"""
        with self.assertRaises(ValueError):
            word_frequency_counter(12345)

    def test_with_whitespace(self):
        """It should handle extra spaces correctly"""
        actual = word_frequency_counter("   Hello   world   ")
        expected = {"hello": 1, "world": 1}
        self.assertEqual(actual, expected)