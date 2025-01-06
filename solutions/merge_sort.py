#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting non empty collection of build-in elementary Python data types
(int, float, string, bool) using merge sort algorithm.
Splitting and sorting function.

Module contents:
    - merge_sort: function that splits the collection and launching the merge.

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""

from solutions.merge import merge


def merge_sort(input_collection: list[any]) -> list[any]:
    """Sort collection using merge sort algorithm.

    Sort elements in collection by splitting the collection in two parts and launching the merge.

    Parameters:
      input_collection: list[any], collection of unsorted data of data types (int, float, string, bool).

    Returns -> list[any], collection of sorted elements of data types (int, float, string, bool).

    Raises:
      AssertionError: if input is not a collection.
      AssertionError: if input collection is empty.
      AssertionError: if input is not a data type processed by module (int, float, string, bool).
      AssertionError: if collection contains elements of different data types (non-homogeneous).

    Examples:
    >>> merge_sort([1])
    [1]
    >>> merge_sort([1, 3, 2])
    [1, 2, 3]
    >>> merge_sort([3, 2, 100500, 1])
    [1, 2, 3, 100500]
    """

    # defensive assertion to check that input is a collection list
    assert isinstance(input_collection, list), "Input is not a collection"

    # defensive assertion to check that input collection is not empty
    assert len(input_collection) > 0, "Collection is empty"

    # defensive assertion to check that input data types are any of (int, float, string, bool)
    assert (
        isinstance(input_collection[0], int)
        or isinstance(input_collection[0], float)
        or isinstance(input_collection[0], str)
        or isinstance(input_collection[0], bool)
    ), "Input data types is not processed. Processed data types (int, float, string, bool)"

    # defensive assertion to check that collection is homogeneous
    assert all(
        isinstance(item, type(input_collection[0])) for item in input_collection
    ), "Collection is not homogeneous"

    # copy collection to avoid side effect
    collection = input_collection.copy()
    if len(collection) < 2:
        return input_collection

    # divide collection to two parts
    split_index = len(collection) // 2

    left = merge_sort(collection[:split_index])
    right = merge_sort(collection[split_index:])

    # return merged collection, sorting left and right parts
    return merge(left, right)
