#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for merging of two sorted collection into one sorted collection.
Processed data types: int, float, string, bool.

Module contents:
    - merge: merge two sorted collections into one sorted collection.

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""


def merge(left: list[any], right: list[any]) -> list[any]:
    """Merge two sorted collections into one sorted collection.

    Combine two sorted homogeneous collections into one sorted collection

    Parameters:
      left: list[any], first sorted collection of data types (int, float, string, bool).
      right: list[any], second sorted collection of data types (int, float, string, bool).

    Returns -> list[any], sorted collection of data types (int, float, string, bool).

    Raises:
      AssertionError: left is not a collection.
      AssertionError: right is not a collection.
      AssertionError: left collection contains elements of different data types (non-homogeneous).
      AssertionError: right collection contains elements of different data types (non-homogeneous).
      AssertionError: left and right contain elements of different data types(non-homogeneous).

    Examples:
    >>> merge([2], [1])
    [1, 2]
    >>> merge([1, 5], [2, 6])
    [1, 2, 5, 6]
    >>> merge([2, 5, 100500], [1, 9])
    [1, 2, 5, 9, 100500]
    """
    # defensive assertion to check that input is a collections are lists
    assert isinstance(left, list), "Input left is not a collection"
    assert isinstance(right, list), "Input right is not a collection"

    # defensive assertion to check that input collections are homogeneous
    assert all(
        isinstance(item, type(left[0])) for item in left
    ), "Input left is not homogeneous"
    assert all(
        isinstance(item, type(right[0])) for item in right
    ), "Input right is not homogeneous"
    assert isinstance(
        left[0], type(right[0])
    ), "Input left and right are not homogeneous"

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
