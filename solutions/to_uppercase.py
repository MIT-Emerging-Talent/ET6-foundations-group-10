#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for converting strings to uppercase.
Module contents:
    - to_uppercase: Converts a given string to uppercase.
Created on 09 Jan 2025
@author: Nimah
"""


def to_uppercase(s: str) -> str:
    """Converts a string to uppercase.
    Parameters:
        s (str): The string to be converted.
    Returns:
        str: The string with all characters in uppercase.
    Raises:
        TypeError: If the input is not a string.
    Examples:
        >>> to_uppercase("hello")
        'HELLO'
        >>> to_uppercase("Python")
        'PYTHON'
        >>> to_uppercase("123abc")
        '123ABC'
        >>> to_uppercase("")
        ''
        >>> to_uppercase("!@#$%^")
        '!@#$%^'
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.upper()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
