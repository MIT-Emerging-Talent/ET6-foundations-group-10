#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the frequency of words in a given sentence.

Features:
    - Handles case-insensitivity
    - Strips punctuation
    - Validates input as a string

Created on 01.01.2025
@author: Ahmad Hamed Dehzad

Examples:
    >>> word_frequency_counter("Hello world hello")
    {'hello': 2, 'world': 1}

    >>> word_frequency_counter("Hello, world! Hello.")
    {'hello': 2, 'world': 1}
"""

import string


def word_frequency_counter(sentence: str) -> dict[str, int]:
    """
    Counts the frequency of each word in a given sentence.

    Args:
        sentence (str): A sentence containing words.

    Returns:
        dict[str, int]: A dictionary where keys are words (case-insensitive)
        and values are their frequency.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(sentence, str):
        raise ValueError("Invalid input: Please enter a text string.")

    # Remove punctuation and split into words
    cleaned_sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_sentence.split()

    # Count word frequencies
    word_frequencies = {}
    for word in words:
        word = word.lower()
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    return word_frequencies
