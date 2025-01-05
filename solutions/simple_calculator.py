#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for performing multiplication, division, summation, or subtraction
operations between two numbers.

Module contents:
    - simple_calculator: performs basic operations on two integers .

Created on 5/1/2024
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""


def simple_calculator(operation: str, operand1: int, operand2: int):
    """
    Parameters:
        operation (str): this is the type of operation we want to perform
                        it should be ('+', '-', '*', or '/')
        operand1 (int): the first number we want to perform the operation on
        operand2 (int): the second number we want
        to perform the operation on, should'nt be zero in division


    Returns-> int or float: the result of the operation on the
                two numbers rounded to three digits if it is a fraction
                or none if the operation is not one of the four basic operations

    Raises:
    AssertionError: if the first argument is not a string
    AssertionError: if the second argument is not an integer
    AssertionError: if the third argument is not an integer
    AssertionError: if the second operand in division is zero

    >>> simple_calculator('+', 3, 8)
    11

    >>> simple_calculator('-', 8, 7)
    1

    >>> simple_calculator('/', 7, 2)
    3.5
    """
    # Ensure inputs are correct
    assert isinstance(operation, str), "operation is not a string"
    assert isinstance(operand1, int), "first number is not an integer"
    assert isinstance(operand2, int), "second number is not an integer"

    # Add the first two operands if the operation is addition
    if operation == "+":
        result = operand1 + operand2

    # Subtract the two operands if the operation is subtraction
    elif operation == "-":
        result = operand1 - operand2

    # Multiply the two operands if the operation is multiplication
    elif operation == "*":
        result = operand1 * operand2

    # Divide the two operands if the operation is division and round the result to three digits
    elif operation == "/":
        # We can't divide by zero
        assert operand2 != 0
        result = round(operand1 / operand2, 3)

    # Return nothing if the operation is not one of the four basic operations
    else:
        result = None

    # Return the result
    return result
