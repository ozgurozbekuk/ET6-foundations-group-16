"""
spiral_traverse.py

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

    This function takes a 2D matrix (a list of lists) and returns a list of its elements 
    arranged in spiral order, starting from the top-left corner and spiraling inward.

    Parameters:
    - matrix (list of list of int or float): A 2D list representing the matrix to traverse.
      The matrix should contain numeric elements (integers or floats).

    Returns:
    - list of int or float: A list of elements from the matrix in spiral order.

    Raises:
    - ValueError: If the input is not a valid 2D list or contains non-numeric elements.

    Example:
    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> spiral_traverse([[1, 2], [3, 4]])
    [1, 2, 4, 3]

    >>> spiral_traverse([[1]])
    [1]
    """
    # Defensive assertions
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a 2D list (matrix).")
    if any(not all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise ValueError("All elements in the matrix must be numeric.")

    result = []  # List to store the elements in spiral order

    while matrix:
        # Add the first row to the result (traverse left to right)
        result += matrix.pop(0)

        # Rotate the remaining matrix counter-clockwise (by transposing and reversing the rows)
        if matrix and matrix[0]:
            matrix = [list(row) for row in zip(*matrix)][::-1]

    return result
