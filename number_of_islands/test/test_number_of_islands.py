import unittest

from number_of_islands.src.number_of_islands import find_num_of_islands


class TestFindNumOfIslands(unittest.TestCase):
    """
    A test suite for the find_num_of_islands function.
    """

    def test_example_case(self):
        """
        Test the example case.
        """
        matrix = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1],
        ]
        # Verify that the function correctly counts 3 islands in the given matrix.
        self.assertEqual(find_num_of_islands(matrix), 3)

    def test_empty_matrix(self):
        """
        Test an empty matrix.
        """
        matrix = []
        # Verify that the function correctly counts 0 islands in an empty matrix.
        self.assertEqual(find_num_of_islands(matrix), 0)

    def test_no_islands(self):
        """
        Test a matrix with no islands.
        """
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # Verify that the function correctly counts 0 islands in a matrix with no islands.
        self.assertEqual(find_num_of_islands(matrix), 0)

    def test_single_island(self):
        """
        Test a matrix with a single island.
        """
        matrix = [[1, 1], [1, 1]]
        # Verify that the function correctly counts 1 island in a matrix with a single island.
        self.assertEqual(find_num_of_islands(matrix), 1)

    def test_single_island_with_diagonal(self):
        """
        Test a matrix with a single island where diagonal cells are considered adjacent.
        """
        matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        # Verify that the function correctly counts 1 island when diagonal cells are considered adjacent.
        self.assertEqual(find_num_of_islands(matrix), 1)


if __name__ == "__main__":
    unittest.main()
