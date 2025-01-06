#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting collection using merge sort algorithm.
Splitting and sorting function.

Module contents:
    - merge_sort: splitting the collection and launching the merge.

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""

from solutions.merge import merge


def merge_sort(input_collection: list[any]) -> list[any]:
    """Sort collection using merge sort algorithm.

    Sort elements in collection by splitting the collection in two parts and launching the merge.

    Parameters:
      input_collection: list[any], collection of unsorted data type any.

    Returns -> list[any], collection of sorted elements with type any.

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
    collection = input_collection.copy()
    if len(collection) < 2:
        return input_collection

    # divide collection to two parts
    split_index = len(collection) // 2

    left = merge_sort(collection[:split_index])
    right = merge_sort(collection[split_index:])

    # return merged collection, sorting left and right parts
    return merge(left, right)
