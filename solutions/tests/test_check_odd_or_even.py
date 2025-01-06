import unittest

from solutions.check_odd_or_even import check_odd_or_even


class TestCheckOddOrEven(unittest.TestCase):
    """Test suite for the check_odd_or_even function."""

    # Standard test cases
    def test_even_number(self):
        """It should return 'Even' for an even integer."""
        self.assertEqual(check_odd_or_even(4), "Even")

    def test_odd_number(self):
        """It should return 'Odd' for an odd integer."""
        self.assertEqual(check_odd_or_even(7), "Odd")

    # Edge cases
    def test_zero(self):
        """It should return 'Even' for zero."""
        self.assertEqual(check_odd_or_even(0), "Even")

    def test_negative_even(self):
        """It should return 'Even' for a negative even number."""
        self.assertEqual(check_odd_or_even(-10), "Even")

    def test_negative_odd(self):
        """It should return 'Odd' for a negative odd number."""
        self.assertEqual(check_odd_or_even(-3), "Odd")


if __name__ == "__main__":
    unittest.main()
