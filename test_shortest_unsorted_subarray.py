"""
Unit tests for the shortest_unsorted_subarray.py module.
"""
import unittest
from shortest_unsorted_subarray import find_shortest_unsorted_subarray


class TestFindShortestUnsortedSubarray(unittest.TestCase):

    """
    Test class for the find_shortest_unsorted_subarray() function.
    """

    def test_unsorted_array(self):
        """
        Test case for an unsorted array.
        :return: None
        """
        input_arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        expected_output = (3, 9)
        self.assertEqual(find_shortest_unsorted_subarray(input_arr), expected_output)

    def test_reverse_sorted_array(self):
        """
        Test case for a reverse sorted array.
        :return: None
        """
        input_arr = [5, 4, 3, 2, 1]
        expected_output = (0, 4)
        self.assertEqual(find_shortest_unsorted_subarray(input_arr), expected_output)

    def test_sorted_array(self):
        """
        Test case for a sorted array.
        :return:
        """
        input_arr = [1, 2, 3, 4, 5]
        expected_output = (-1, -1)
        self.assertEqual(find_shortest_unsorted_subarray(input_arr), expected_output)

    def test_single_element_array(self):
        """
        Test case for a single element array.
        :return:
        """
        input_arr = [1]
        expected_output = (-1, -1)
        self.assertEqual(find_shortest_unsorted_subarray(input_arr), expected_output)

    def test_empty_array(self):
        """
        Test case for an empty array.
        :return:
        """
        input_arr = []
        expected_output = (-1, -1)
        self.assertEqual(find_shortest_unsorted_subarray(input_arr), expected_output)


if __name__ == '__main__':
    unittest.main()
