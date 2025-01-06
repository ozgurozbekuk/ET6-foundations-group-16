#!/usr/bin/env python3
"""
A module for determining if a number is even or odd.

Module contents:
    - check_odd_or_even: Returns "Even" if the number is even, "Odd" otherwise.
"""


def check_odd_or_even(num):
    """Checks if the provided integer is even or odd.

    Parameters:
        num (int): The integer to check.

    Returns:
        str: "Even" if num is even, otherwise "Odd".

    Raises:
        AssertionError: If num is not an integer.
    """
    assert isinstance(num, int), "num must be an integer"
    return "Even" if num % 2 == 0 else "Odd"
