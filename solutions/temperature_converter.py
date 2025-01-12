#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting temperatures between Celsius and Fahrenheit.

Module contents:
    - celsius_to_fahrenheit: Converts a temperature from Celsius to Fahrenheit.
    - fahrenheit_to_celsius: Converts a temperature from Fahrenheit to Celsius.

Created on 01.05.2025
@author: Ahmad Hamed Dehzad
"""

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit.

    Parameters:
        celsius: float, the temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.

    Raises:
        ValueError: If the input is not a number.

    >>> celsius_to_fahrenheit(0)
    32.0

    >>> celsius_to_fahrenheit(100)
    212.0

    >>> celsius_to_fahrenheit(-40)
    -40.0
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Invalid input: Temperature must be a number.")

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit: float, the temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.

    Raises:
        ValueError: If the input is not a number.

    >>> fahrenheit_to_celsius(32)
    0.0

    >>> fahrenheit_to_celsius(212)
    100.0

    >>> fahrenheit_to_celsius(-40)
    -40.0
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Invalid input: Temperature must be a number.")

    return (fahrenheit - 32) * 5 / 9