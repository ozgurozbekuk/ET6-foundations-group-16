#!/usr/bin/env python3

"""
A module for converting decimal numbers to binary.

Module contents:
    - decimal_to_binary: Converts a decimal number to its binary equivalent.

Author: Anas Ziadah
Created: 2025-01-07
"""


def decimal_to_binary(decimal: int) -> str:
    """Converts a decimal number to its binary equivalent.

    The conversion is done using the division-by-2 method. Raises an error for negative numbers.

    Parameters:
        decimal: int, the decimal number to convert.

    Returns:
        str: The binary equivalent of the decimal number as a string.

    Raises:
        ValueError: If the decimal number is negative.

    Examples:
        >>> decimal_to_binary(10)
        '1010'
        >>> decimal_to_binary(5)
        '101'
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(255)
        '11111111'
    """

    if decimal < 0:
        raise ValueError("Negative numbers are not supported.")

    if decimal == 0:
        return "0"

    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return binary
