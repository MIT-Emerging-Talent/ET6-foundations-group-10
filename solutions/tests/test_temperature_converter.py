#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a test module for converting temperatures between Celsius and Fahrenheit.

Test categories:
    - Standard cases: typical temperature values
    - Edge cases: extreme temperatures and boundary values
    - Defensive tests: non-numeric inputs

Created on 01.05.2025

@author: Ahmad Hamed Dehzad
"""

import unittest

from ..temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):
    """Test the temperature conversion functions"""

    # Tests for celsius_to_fahrenheit
    def test_celsius_to_fahrenheit_zero(self):
        """It should convert 0°C to 32°F"""
        actual = celsius_to_fahrenheit(0)
        expected = 32.0
        self.assertEqual(actual, expected)

    def test_celsius_to_fahrenheit_positive(self):
        """It should convert 100°C to 212°F"""
        actual = celsius_to_fahrenheit(100)
        expected = 212.0
        self.assertEqual(actual, expected)

    def test_celsius_to_fahrenheit_negative(self):
        """It should convert -40°C to -40°F"""
        actual = celsius_to_fahrenheit(-40)
        expected = -40.0
        self.assertEqual(actual, expected)

    def test_celsius_to_fahrenheit_non_numeric(self):
        """It should raise a ValueError if the input is not a number"""
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("invalid")

    # Tests for fahrenheit_to_celsius
    def test_fahrenheit_to_celsius_zero(self):
        """It should convert 32°F to 0°C"""
        actual = fahrenheit_to_celsius(32)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_fahrenheit_to_celsius_positive(self):
        """It should convert 212°F to 100°C"""
        actual = fahrenheit_to_celsius(212)
        expected = 100.0
        self.assertEqual(actual, expected)

    def test_fahrenheit_to_celsius_negative(self):
        """It should convert -40°F to -40°C"""
        actual = fahrenheit_to_celsius(-40)
        expected = -40.0
        self.assertEqual(actual, expected)

    def test_fahrenheit_to_celsius_non_numeric(self):
        """It should raise a ValueError if the input is not a number"""
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("invalid")


if __name__ == "__main__":
    unittest.main()