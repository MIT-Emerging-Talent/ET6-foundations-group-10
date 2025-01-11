#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for converting strings to uppercase.

Module contents:
    - to_uppercase: Converts a given string to uppercase.

Created on XX XX XX
@author: Your Name
"""


def to_uppercase(s: str) -> str:
    """Converts a string to uppercase.

    Parameters:
        s (str): The string to be converted.

    Returns:
        str: The string with all characters in uppercase.

    Raises:
        TypeError: If the input is not a string.

    >>> to_uppercase("hello")
    'HELLO'

    >>> to_uppercase("Python")
    'PYTHON'

    >>> to_uppercase("123abc")
    '123ABC'
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.upper()
