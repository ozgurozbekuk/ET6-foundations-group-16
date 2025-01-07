"""
is_palindrome.py
This module provides a function to determine if a string is a palindrome,
ignoring case and non-alphanumeric characters.

Author: Faisal Minawi
Date: Mon Jan 6 2025
Group: ET6-foundations-group-16

Functions:
- is_palindrome(s): Determines if a given string is a palindrome.
"""


def is_palindrome(s):
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.

    Parameters:
    - s (str): Input string to check.

    Returns:
    - bool: True if the string is a palindrome, False otherwise.

    Raises:
    - TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome(" ")
        True
        >>> is_palindrome("Madam")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome(None)
        Traceback (most recent call last):
            ...
        TypeError: Input must be a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Convert to lowercase and keep only alphanumeric characters
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    # Compare the string with its reverse
    return cleaned == cleaned[::-1]
