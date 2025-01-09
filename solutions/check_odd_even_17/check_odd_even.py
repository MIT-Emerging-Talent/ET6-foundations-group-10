#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module contains a function to identify if a number is even or odd."""


def check_odd_even(number):
    """Check if the number is odd or even."""
    if number % 2 == 0:
        return "even_number"

    return "odd_number"


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        RESULT = check_odd_even(num)
        print(f"The number {num} is {RESULT}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
