#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test nodule for basic_calculator function

Test categories:
 -Standard cases: typical inputs
 -Edge cases: extreme inputs and boundaries
 -Defensive tests: wrong input types, assertions

Created on 5/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""

import unittest

from ..simple_calculator import simple_calculator


class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the basic_calculator function"""

    # Standard test cases
    def test_addition_normal_inputs(self):
        """it should add the two numbers"""
        self.assertEqual(simple_calculator("+", 3, 8), 11)

    def test_subtraction_normal_inputs(self):
        """it should subtract the two numbers"""
        self.assertEqual(simple_calculator("-", 8, 7), 1)

    def test_division_normal_inputs_result_is_fraction(self):
        """it should perform division on the two numbers,
        the first devised by the second and return float if the result is a fraction"""
        self.assertEqual(simple_calculator("/", 7, 2), 3.5)

    def test_multiplication_normal_inputs(self):
        """it should multiply the two numbers"""
        self.assertEqual(simple_calculator("*", 7, 17), 119)

    # Edge cases

    def test_multiplication_large_numbers(self):
        """it should multiply the two numbers"""
        self.assertEqual(simple_calculator("*", 257753347, 1000000), 257753347000000)

    def test_division_large_numbers(self):
        """it should perform division between the two numbers"""
        self.assertEqual(simple_calculator("/", 2577533479764, 7872764782), 327.399)

    def test_undefined_operation(self):
        """it should return nothing if the operation is not one of
        the four basic operations"""
        self.assertEqual(simple_calculator("**", 9, 2), None)

    def test_negative_numbers(self):
        """it should perform operations on negative numbers"""
        self.assertEqual(simple_calculator("*", 23, -2), -46)

    # Defensive tests
    def test_non_string_input_operation(self):
        """It should raise AssertionError if input operation is not a string"""
        with self.assertRaises(AssertionError):
            simple_calculator(2, 3, 5)

    def test_non_integer_input_first_operand(self):
        """It should raise AssertionError if first operand is not an integer"""
        with self.assertRaises(AssertionError):
            simple_calculator("*", 3.78, 45)

    def test_non_integer_input_second_operand(self):
        """It should raise AssertionError if second operand is not an integer"""
        with self.assertRaises(AssertionError):
            simple_calculator("*", 3, 45.876)

    def test_division_by_zero(self):
        """It should raise AssertionError if second operand in division_is_zero"""
        with self.assertRaises(AssertionError):
            simple_calculator("/", 38, 0)
