#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for merging of two sorted collection into one sorted collection.

Module contents:
    - merge: merge two sorted collections into one sorted collection.

Created on 2024-01-06
Author: Oleksandr Maksymikhin
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted collections into one sorted collection.

    Combine two sorted homogeneous collections into one sorted collection

    Parameters:
      left: list[int], first sorted collection of type int.
      right: list[int], second sorted collection of type int.

    Returns -> list[int], collection of sorted elements with type int.

    Raises:
      AssertionError: left is not a collection.
      AssertionError: right is not a collection.
      AssertionError: left collection contains elements of different data types (non-homogeneous).
      AssertionError: right collection contains elements of different data types (non-homogeneous).
      AssertionError: data of left and right collections have different types (non-homogeneous).

    Examples:
    >>> merge([2], [1])
    [1, 2]
    >>> merge_sort([1, 5], [2, 6])
    [1, 2, 5, 6]
    >>> merge_sort([2, 5, 100500], [1, 9])
    [1, 2, 5, 9, 100500]
    """

    return left + right
