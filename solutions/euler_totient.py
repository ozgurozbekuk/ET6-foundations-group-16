"""
euler_totient.py

This module provides a function to compute Euler's totient function (ϕ(n)),
which counts the number of integers between 1 and n inclusive, that are coprime to n.

Author: Fahed Daibes
Date: Mon Jan 6 2025
Group: ET6-foundations-group-16

Functions:
- euler_totient(n): Computes Euler's totient function (ϕ(n)) for a given integer n.
"""


def euler_totient(n):
    """
    Euler's totient function or Phi function.

    Parameters:
    - n (int): A positive integer for which the Euler's totient function is to be computed.

    Returns:
    - int: The number of integers between 1 and n inclusive that are coprime to n.

    Raises:
    - ValueError: If the input is not a positive integer.

    Examples:
        >>> euler_totient(5)
        4
        >>> euler_totient(1)
        1
        >>> euler_totient(10)
        4
        >>> euler_totient(0)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> euler_totient(-5)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result
