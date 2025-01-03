#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting collection using bubble sort algorithm.

Module contents:
    - bubble_sort: sort the collection in ascending order.

Created on 2024-01-02
Author: Oleksandr Maksymikhin
"""


# def bubble_sort(input_collection: list[int]) -> list[int]:
def bubble_sort(input_collection: list[any]) -> list[any]:
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
    collection = input_collection
    # define collection length
    collection_length = len(collection)
    # first loop to traverse the collection
    for current_item_index in range(collection_length):
        # flag to break if the last run didn't swap any item
        already_sorted = True
        # second loop to compare item with adjacent one
        for swap_index in range(collection_length - current_item_index - 1):
            # swap items if next adjacent item is bigger
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
