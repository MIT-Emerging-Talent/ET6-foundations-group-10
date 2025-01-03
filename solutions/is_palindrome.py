#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a string is a palindrome.

Module contents:
    - is_palindrome: Checks if a given string is a palindrome.

Created on 2024-12-30
Author: Emre Biyik
"""


def is_palindrome(text: str) -> bool:
    """Checks if a string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring case and spaces.

    Parameters:
        text: str, the input string to check.

    Returns -> bool: True if the input is a palindrome, False otherwise.

    Raises:
        AssertionError: if input is not a string.

    Examples:
        >>> is_palindrome("level")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Ensure the input is of type string to avoid unexpected errors.
    assert isinstance(text, str), "Input must be a string"

    # Normalize the text: remove spaces and convert to lowercase
    normalized = "".join(char.lower() for char in text if char.isalnum())

    # Check if the string is the same when reversed
    return normalized == normalized[::-1]
