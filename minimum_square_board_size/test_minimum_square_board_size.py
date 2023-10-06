"""
Unit tests for the minimum_square_board_size.py module.
"""

import unittest
from minimum_square_board_size import get_board_size


class TestGetBoardSize(unittest.TestCase):
    """
    Test class for the get_board_size() function.
    """

    def test_example_1(self):
        """
        Test case for example 1.
        :return: None
        """
        w = 2
        h = 3
        N = 10
        expected_output = 9
        self.assertEqual(get_board_size(w, h, N), expected_output)

    def test_example_2(self):
        """
        Test case for example 2.
        :return: None
        """
        w = 3
        h = 2
        N = 10
        expected_output = 9
        self.assertEqual(get_board_size(w, h, N), expected_output)

    def test_example_3(self):
        """
        Test case for example 3.
        :return: None
        """

        w = 1
        h = 1
        N = 4

        expected_output = 2
        self.assertEqual(get_board_size(w, h, N), expected_output)

    def test_example_4(self):
        """
        Test case for example 4.
        :return: None
        """

        w = 1
        h = 1
        N = 5

        expected_output = 3
        self.assertEqual(get_board_size(w, h, N), expected_output)

    def test_example_5(self):
        """
        Test case for example 5.
        :return: None
        """

        w = 999999999
        h = 1000000000
        N = 2

        expected_output = 1999999998
        self.assertEqual(get_board_size(w, h, N), expected_output)
