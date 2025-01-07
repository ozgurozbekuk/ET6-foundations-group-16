#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_palindrome function.

Test categories:
    - Standard cases: various palindromes and non-palindromes
    - Edge cases: empty strings, spaces, special characters
    - Defensive tests: wrong input types
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test suite for the is_palindrome function."""

    # Standard test cases
    def test_simple_palindromes(self):
        """It should identify simple palindromes correctly."""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindromes(self):
        """It should identify non-palindromes correctly."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("12345"))

    def test_case_sensitivity(self):
        """It should ignore case when checking palindromes."""
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("RaCeCaR"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

    # Edge cases
    def test_empty_and_spaces(self):
        """It should handle empty strings and spaces correctly."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("   "))

    def test_special_characters(self):
        """It should ignore special characters and spaces."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Race fast, safe car!"))
        self.assertFalse(is_palindrome("race a car"))

    def test_single_character(self):
        """It should handle single-character strings."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("5"))
        self.assertTrue(is_palindrome("!"))

    # Defensive tests
    def test_invalid_input_none(self):
        """It should raise TypeError for None input."""
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_invalid_input_types(self):
        """It should raise TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(["a", "b", "c"])
        with self.assertRaises(TypeError):
            is_palindrome(True)


if __name__ == "__main__":
    unittest.main()
