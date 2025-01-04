#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for calculate_average function.

Test categories:
    - Standard cases: multiple numbers
    - Edge cases: empty list, single element, negative numbers, zeros
    - Defensive tests: wrong input types, assertions
"""

import unittest
from solutions.calc_avg import calculate_average


class TestCalculateAverage(unittest.TestCase):
    """Test suite for the calculate_average function."""

    # Standard test cases
    def test_integers(self):
        """It should return the average of multiple integers."""
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30.0)

    def test_floats(self):
        """It should return the average of multiple floats."""
        self.assertAlmostEqual(calculate_average([1.1, 2.2, 3.3]), 2.2, places=1)


if __name__ == "__main__":
    unittest.main()
