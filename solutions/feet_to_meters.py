#!/usr/bin/env python3
"""
Module to convert feet to meters.

The conversion factor from feet to meters is:
    1 foot = 0.3048 meters

Author: Obay Salih
Date: 8th January 2025
"""


def feet_to_meters(feet: float) -> float:
    """
    Converts a length from feet to meters.

    Parameters:
        feet (float): The length in feet.

    Returns:
        float: The equivalent length in meters.

    Raises:
        AssertionError: If feet is not a number.

    Examples:
        >>> feet_to_meters(1)
        0.3048
        >>> feet_to_meters(10)
        3.048
        >>> feet_to_meters(0)
        0.0
        >>> feet_to_meters(-5)
        -1.524
        >>> feet_to_meters("10")  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError: feet must be a number
    """
    assert isinstance(feet, (int, float)), "feet must be a number"
    return feet * 0.3048
