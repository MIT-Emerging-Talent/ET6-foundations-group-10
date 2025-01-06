#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting collection using merge sort algorithm.
Splitting and sorting function.

Module contents:
    - merge_sort: splitting the collection and launching the merge.

Created on 2024-01-06
Author: Oleksandr Maksymikhin
"""

from .merge import merge


def merge_sort(input_collection: list[int]) -> list[int]:
    """Sort collection using merge sort algorithm.

    Sort elements in collection by splitting the collection in two parts and launching the merge.

    Parameters:
      input_collection: list[int], collection of unsorted data type int.

    Returns -> list[int], collection of sorted elements with type int.

    Raises:
      AssertionError: if input is not a collection.
      AssertionError: if collection contains elements of different data types (non-homogeneous).

    Examples:
    >>> merge_sort([1])
    [1]
    >>> merge_sort([1, 3, 2])
    [1, 2, 3]
    >>> merge_sort([3, 2, 100500, 1])
    [1, 2, 3, 100500]
    """

    merge([1], [2])
    return input_collection
