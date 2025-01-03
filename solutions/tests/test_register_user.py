#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for register_user function.

Test categories:
    - Standard cases: valid inputs
    - Edge cases: minimum and maximum valid ages
    - Defensive tests: invalid inputs for name, age, and email

Created on: 2025-01-03
Author: Emre Biyik
"""

import unittest
from solutions.register_user import register_user


class TestRegisterUser(unittest.TestCase):
    """Test suite for the register_user function."""

    # Standard cases
    def test_valid_inputs(self):
        """It should register a user with valid details."""
        result = register_user("Alice", 25, "alice@example.com")
        expected = {"name": "Alice", "age": 25, "email": "alice@example.com"}
        self.assertEqual(result, expected)

    # Edge cases
    def test_minimum_age(self):
        """It should allow the minimum valid age."""
        self.assertEqual(
            register_user("Bob", 18, "bob@example.net"),
            {"name": "Bob", "age": 18, "email": "bob@example.net"},
        )

    def test_maximum_age(self):
        """It should allow the maximum valid age."""
        self.assertEqual(
            register_user("Charlie", 99, "charlie@example.org"),
            {"name": "Charlie", "age": 99, "email": "charlie@example.org"},
        )

    # Defensive tests
    def test_invalid_name(self):
        """It should raise ValueError for invalid names."""
        with self.assertRaises(ValueError):
            register_user("Alice123", 25, "alice@example.com")

    def test_invalid_age_below_minimum(self):
        """It should raise ValueError for ages below 18."""
        with self.assertRaises(ValueError):
            register_user("Alice", 17, "alice@example.com")

    def test_invalid_age_above_maximum(self):
        """It should raise ValueError for ages above 99."""
        with self.assertRaises(ValueError):
            register_user("Alice", 100, "alice@example.com")

    def test_invalid_email_format(self):
        """It should raise ValueError for invalid email formats."""
        with self.assertRaises(ValueError):
            register_user("Alice", 25, "aliceexample.com")

    def test_multiple_invalid_inputs(self):
        """It should raise ValueError for multiple invalid inputs."""
        with self.assertRaises(ValueError):
            register_user("Alice123", 17, "aliceexample.com")


if __name__ == "__main__":
    unittest.main()
