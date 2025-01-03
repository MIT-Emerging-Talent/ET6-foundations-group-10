#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for registering users with validated inputs.

Module contents:
    - register_user: Validates user details and returns a registration dictionary.

Created on: 2025-01-03
Author: Emre Biyik
"""


def register_user(name: str, age: int, email: str) -> dict:
    """
    Registers a user with the given name, age, and email.

    Parameters:
        name (str): User's name. Must contain only alphabetic characters.
        age (int): User's age. Must be between 18 and 99 (inclusive).
        email (str): User's email. Must be in a valid format.

    Returns:
        dict: A dictionary containing the user's details.

    Raises:
        ValueError: If `name`, `age`, or `email` is invalid.

    Examples:
        >>> register_user("Alice", 25, "alice@example.com")
        {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

        >>> register_user("Bob", 18, "bob@example.net")
        {'name': 'Bob', 'age': 18, 'email': 'bob@example.net'}

    """
    if not name.isalpha():
        raise ValueError("Invalid name: Must contain only alphabetic characters.")
    if not isinstance(age, int) or not (18 <= age <= 99):
        raise ValueError("Invalid age: Must be an integer between 18 and 99.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Invalid email: Must be a valid email format.")

    return {"name": name, "age": age, "email": email}
