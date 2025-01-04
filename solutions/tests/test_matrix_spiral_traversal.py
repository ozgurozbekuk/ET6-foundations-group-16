import unittest

from solutions.matrix_spiral_traversal import spiral_traverse


class TestSpiralTraversal(unittest.TestCase):
    def test_square_matrix(self):
        """Test case for a square matrix."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_single_row(self):
        """Test case for a single-row matrix."""
        matrix = [[1, 2, 3, 4]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 4])

    def test_single_column(self):
        """Test case for a single-column matrix."""
        matrix = [[1], [2], [3], [4]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 4])

    def test_rectangular_matrix(self):
        """Test case for a rectangular matrix."""
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(spiral_traverse(matrix), [1, 2, 3, 6, 5, 4])

    def test_empty_matrix(self):
        """Test case for an empty matrix."""
        matrix = []
        self.assertEqual(spiral_traverse(matrix), [])

    def test_single_element_matrix(self):
        """Test case for a single-element matrix."""
        matrix = [[1]]
        self.assertEqual(spiral_traverse(matrix), [1])


if __name__ == "__main__":
    unittest.main()
