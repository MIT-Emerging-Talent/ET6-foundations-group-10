#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for merging of two sorted collection into one sorted collection.

Module contents:
    - merge: merge two sorted collections into one sorted collection.

Created on 2024-01-05
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
    >>> merge([1, 5], [2, 6])
    [1, 2, 5, 6]
    >>> merge([2, 5, 100500], [1, 9])
    [1, 2, 5, 9, 100500]
    """
    # check if left or right collection is empty
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    # create empty collection for merge
    merged_collection = []
    # create indexed to traverse collections
    index_left = index_right = 0

    # merge collections until length of merged collection is smaller
    # then length of left and right collections
    while len(merged_collection) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            merged_collection.append(left[index_left])
            index_left += 1
        else:
            merged_collection.append(right[index_right])
            index_right += 1

        # if left or right collection becomes empty
        # add elements of the other collection and break loop
        if index_left == len(left):
            merged_collection += right[index_right:]
            break
        if index_right == len(right):
            merged_collection += left[index_left:]
            break

    return merged_collection
