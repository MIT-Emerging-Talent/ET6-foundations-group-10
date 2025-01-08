#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting non empty collection of build-in elementary Python data types
(int, float, str, bool) using merge sorting algorithm.

Module contents:
    - merge_sort: function that splits the collection and launches the merge.
    - merge: function that merges two sorted collections into one sorted collection.

Created on 2024-01-05
Author: Oleksandr Maksymikhin
"""

from typing import TypeVar

# from solutions.merge import merge

T = TypeVar("T", int, float, str, bool)


def merge_sort(input_collection: list[T]) -> list[T]:
    """Sort collection using merge sorting algorithm.

    Sort elements in collection by splitting the collection in two parts and launch merge.

    Parameters:
      input_collection: list[T], collection of unsorted elements of data types (int, float, string, bool).

    Returns -> list[T], collection of sorted elements of data types (int, float, string, bool).

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
    >>> merge_sort(['banana', 'apple', 'cherry'])
    ['apple', 'banana', 'cherry']
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


def merge(left: list[T], right: list[T]) -> list[T]:
    """Merge two sorted collections into one sorted collection.

    Combine two sorted homogeneous collections into one sorted collection

    Parameters:
      left: list[T], first sorted collection of data types (int, float, string, bool).
      right: list[T], second sorted collection of data types (int, float, string, bool).

    Returns -> list[T], sorted collection of data types (int, float, string, bool).

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
