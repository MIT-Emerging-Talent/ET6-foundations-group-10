#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting collection using bubble sort algorithm.

Module contents:
    - bubble_sort: sort the collection in ascending order.

Created on 2024-01-02
Author: Oleksandr Maksymikhin
"""


def bubble_sort(input_collection: list[int]) -> list[int]:
    """Sort collection using bubble sort algorithm.

    Sort elements in collection by swapping and moving larger elements to the end of collection.

    Parameters:
      input_collection: list[int], collection of unsorted data type int.

    Returns -> list[int], collection of sorted data type int.

    Raises:
      AssertionError: if collection contains elements of different type.

    Examples:
    >>> bubble_sort(1)
    [1]
    >>> bubble_sort([1, 3, 2]])
    [1, 2, 3]
    >>> bubble_sort([3, 2, 1000000, 1]])
    [1, 2, 3, 1000000]
    """
    # add return statement to avoid lint errors
    output_collection = input_collection
    return output_collection
