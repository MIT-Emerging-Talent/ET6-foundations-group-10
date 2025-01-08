#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting collection using bubble sort algorithm.
Processed types: int, float, str, bool

Module contents:
    - bubble_sort: sort the collection in ascending order.

Created on 2024-01-02
Author: Oleksandr Maksymikhin
"""

from typing import TypeVar

T = TypeVar("T", int, float, str, bool)


# def bubble_sort(input_collection: list[int]) -> list[int]:
def bubble_sort(input_collection: list[T]) -> list[T]:
    """Sort collection using bubble sort algorithm.

    Sort elements in collection by swapping and moving larger elements to the end of collection.

    Parameters:
      input_collection: list[T], collection of unsorted data with data types (T): int, float, str, bool.

    Returns -> list[T], collection of sorted elements with data types (T): int, float, str, bool.

    Raises:
      AssertionError: if input is not a collection.
      AssertionError: if collection contains elements of different data types (non-homogeneous).

    Examples:
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([1, 3, 2])
    [1, 2, 3]
    >>> bubble_sort([3, 2, 100500, 1])
    [1, 2, 3, 100500]
    """

    # defensive assertion to check that input is a collection list
    assert isinstance(input_collection, list), "Input is not a collection"

    # defensive assertion to check that collection is homogeneous
    assert all(
        isinstance(item, type(input_collection[0])) for item in input_collection
    ), "Input collection is not homogeneous"

    # copy collection to avoid side effect
    collection = input_collection.copy()
    # define collection length
    collection_length = len(collection)
    # first loop to traverse the collection
    for current_item_index in range(collection_length):
        # flag to break if the last run didn't swap any item
        already_sorted = True
        # second loop to compare/swap item with adjacent one
        for swap_index in range(collection_length - current_item_index - 1):
            # swap items if the next adjacent item is smaller
            if collection[swap_index] > collection[swap_index + 1]:
                (collection[swap_index], collection[swap_index + 1]) = (
                    collection[swap_index + 1],
                    collection[swap_index],
                )
                already_sorted = False
        # break loop if the last run didn't swap any item
        if already_sorted:
            break
    # return sorted collection
    return collection
