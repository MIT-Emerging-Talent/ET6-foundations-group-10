#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to format a number and determine if it is an odd or even number.
The function takes an integer as input and returns a string indicating whether the number is odd or even.
"""


def check_odd_even(number: int) -> str:
    """
    Determine if a number is odd or even.
    Args:
        number (int): The integer to check.
    Returns:
        str: "even_number" if the number is even, "odd_number" if the number is odd.
    Example:
    >>> check_odd_even(5)
    'odd_number'
    >>> check_odd_even(2)
    'even_number'
    """
    if number % 2 == 0:
        return "even_number"
    return "odd_number"
