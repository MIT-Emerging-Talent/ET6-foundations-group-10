#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for validating user registration inputs.

Module contents:
    - register_user: Validates user details and returns a registration dictionary.

Created on: 2025-01-03
Author: Emre Biyik
"""


def register_user(name: str, age: int, email: str) -> dict:
    """
    Validates the parameters (name, age, email) provided for user registration.

    Parameters:
        name (str): User's name. Must contain only alphabetic characters.
        age (int): User's age. Must be between 18 and 99 (inclusive).
        email (str): User's email. Must be in a valid format.

    Returns:
        dict: A dictionary containing the user's details.

    Raises:
        ValueError: If name contains non-alphabetic characters.
        ValueError: If age is under 18 or over 99 years old.
        ValueError: If email does not include symbols "@" and "." (in the part after the "@" separator).

    Examples:
        >>> register_user("Alice", 25, "alice@example.com")
        {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

        >>> register_user("Bob", 18, "bob@example.net")
        {'name': 'Bob', 'age': 18, 'email': 'bob@example.net'}

        >>> register_user("Dave", 30, "dave@example.org")
        {'name': 'Dave', 'age': 30, 'email': 'dave@example.org'}
    """
    # Check if name contains only alphabetic characters
    if not name.isalpha():
        raise ValueError("Invalid name: Must contain only alphabetic characters.")

    # Check if age is within the valid range (18-99)
    if not isinstance(age, int) or not (18 <= age <= 99):
        raise ValueError("Invalid age: Must be an integer between 18 and 99.")

    # Check if email contains "@" and "."
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Invalid email: Must be a valid email format.")

    return {"name": name, "age": age, "email": email}
