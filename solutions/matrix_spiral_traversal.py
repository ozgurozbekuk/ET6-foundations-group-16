"""
matrix_spiral_traversal.py

This module provides a function to traverse a 2D matrix in spiral order.

Author: Fahed Daibes
Date: Sat Jan 4 2025
Group: ET6-foundations-group-16

Functions:
- spiral_traverse(matrix): Traverses a matrix in spiral order and returns the result.
"""


def spiral_traverse(matrix):
    """
    Traverse a 2D matrix in spiral order.

    Parameters:
    - matrix (list of list of int): A 2D list representing the matrix to traverse.

    Returns:
    - list of int: A list of elements from the matrix in spiral order.

    Example:
    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    result = []

    while matrix:
        # Add the first row to the result
        result += matrix.pop(0)

        # Rotate the remaining matrix counter-clockwise
        if matrix and matrix[0]:
            matrix = [list(row) for row in zip(*matrix)][::-1]

    return result
