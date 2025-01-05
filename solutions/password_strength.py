#!/usr/bin/env python3

"""
A module for checking the strength of a password.

Module contents:
    - check_password_strength: Checks the strength of a given password.

Author: Anas Ziadah
Created: 2025-01-05
"""

import re


def check_password_strength(password):
    """Checks the strength of a given password.

    The password strength is determined by the following rules:
    - Minimum length of 8 characters.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    - Must contain at least one special character (e.g., @, #, $, etc.).

    Parameters:
        password: str, the password to check.

    Returns:
        str: A message indicating whether the password is strong or not.

    Raises:
        ValueError: if the password does not meet the strength requirements.

    Examples:
        >>> check_password_strength("StrongP@ssw0rd")
        'Strong password'
        >>> check_password_strength("weakpass")
        'Weak password'
        >>> check_password_strength("Short1!")
        'Weak password'
        >>> check_password_strength("NoSpecial123")
        'Weak password'
    """

    if len(password) < 8:
        raise ValueError("Password is too short. Minimum length is 8 characters.")

    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit.")

    if not re.search(r"[@$!%*?&]", password):
        raise ValueError("Password must contain at least one special character.")

    return "Strong password"
