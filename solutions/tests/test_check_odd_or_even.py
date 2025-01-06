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


if __name__ == "__main__":
    unittest.main()
