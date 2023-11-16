import os
import tempfile
import unittest

from smallest_number_of_beer_types.src.smallest_number_of_beer_types import convert_line_to_binary_array, \
    transform_preferences, min_beers, read_beer_preferences


class TestBeerPreferences(unittest.TestCase):
    def setUp(self):
        self.temp_fd, self.temp_path = tempfile.mkstemp()

    def tearDown(self):
        os.close(self.temp_fd)
        os.remove(self.temp_path)

    def test_example_1(self):
        # Test with the first example
        with open(self.temp_path, 'w') as temp_file:
            temp_file.write(
                "2 2\nYN NY"
            )

        num_of_employees, num_of_beers, preferences_line = read_beer_preferences(self.temp_path)

        array = convert_line_to_binary_array(preferences_line, num_of_beers)

        adjacency_list_of_beer_preferences = transform_preferences(array)

        result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)

        self.assertEqual(result, 2)

    def test_example_2(self):
        # Test with the second example
        with open(self.temp_path, 'w') as temp_file:
            temp_file.write("6 3\nYNN YNY YNY NYY NYY NYN")

        num_of_employees, num_of_beers, preferences_line = read_beer_preferences(self.temp_path)

        array = convert_line_to_binary_array(preferences_line, num_of_beers)

        adjacency_list_of_beer_preferences = transform_preferences(array)

        result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)

        self.assertEqual(result, 2)

    def test_example_3(self):
        # Test with the third example
        with open(self.temp_path, 'w') as temp_file:
            temp_file.write("4 3\nYYN YYN YYN NNY")

        num_of_employees, num_of_beers, preferences_line = read_beer_preferences(self.temp_path)

        array = convert_line_to_binary_array(preferences_line, num_of_beers)

        adjacency_list_of_beer_preferences = transform_preferences(array)
        result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)

        self.assertEqual(result, 2)

    def test_example_4(self):
        # Test with the fourth example
        with open(self.temp_path, 'w') as temp_file:
            temp_file.write("4 4\n YNNN NYNN NNYN NNNY")

        num_of_employees, num_of_beers, preferences_line = read_beer_preferences(self.temp_path)

        array = convert_line_to_binary_array(preferences_line, num_of_beers)

        adjacency_list_of_beer_preferences = transform_preferences(array)
        result = min_beers(num_of_employees, adjacency_list_of_beer_preferences)

        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
