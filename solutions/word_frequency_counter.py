#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the frequency of words in a given sentence.

Module contents:
    - word_frequency_counter: calculates the frequency of each word in a sentence.
    - display_word_frequencies: prints the word frequencies in a readable format.

Created on 01.01.2025
@author: Ahmad Hamed Dehzad
"""

# def word_frequency_counter(sentence):
#     if not isinstance(sentence, str):
#         raise ValueError("Invalid input: Please enter a text string.")
#     words = sentence.split()
#     word_frequencies = {}
#     for word in words:
#         word = word.lower()
#         if word in word_frequencies:
#             word_frequencies[word] += 1
#         else:
#             word_frequencies[word] = 1
#     return word_frequencies


# --- after documenting and testing ---

def word_frequency_counter(sentence: str) -> dict[str, int]:
    """Counts the frequency of each word in a given sentence.

    Parameters:
        sentence: str, a sentence containing words separated by spaces.

    Returns:
        A dictionary where keys are words (case-insensitive) and values are their frequency.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(sentence, str):
        raise ValueError("Invalid input: Please enter a text string.")

    words = sentence.split()
    word_frequencies = {}
    for word in words:
        word = word.lower()
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    return word_frequencies