#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the to_uppercase function.

Created on 11 01 2025
@author: Nimah Masuud
"""

import unittest
from solutions.to_uppercase import to_uppercase


class TestToUppercase(unittest.TestCase):
    """Tests for the to_uppercase function."""

    def test_valid_string(self):
        """It should convert lowercase to uppercase."""
        self.assertEqual(to_uppercase("hello"), "HELLO")

    def test_mixed_case_string(self):
        """It should convert mixed case to uppercase."""
        self.assertEqual(to_uppercase("Python"), "PYTHON")

    def test_alphanumeric_string(self):
        """It should handle alphanumeric strings."""
        self.assertEqual(to_uppercase("123abc"), "123ABC")

    def test_empty_string(self):
        """It should return an empty string."""
        self.assertEqual(to_uppercase(""), "")

    def test_non_string_input(self):
        """It should raise TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            to_uppercase(123)


if __name__ == "__main__":
    unittest.main()
