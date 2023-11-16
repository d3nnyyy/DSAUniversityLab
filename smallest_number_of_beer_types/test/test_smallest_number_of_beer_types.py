import os
import tempfile
import unittest

from smallest_number_of_beer_types.src.smallest_number_of_beer_types import (
    execute_beer_preferences,
    NO_BEER_PREFERENCE_MSG, INVALID_NUM_OF_BEERS_MSG, INVALID_NUM_OF_EMPLOYEES_MSG, INVALID_PREFERENCES_LINE_MSG
)


class TestBeerPreferences(unittest.TestCase):
    def setUp(self):
        self.temp_fd, self.temp_path = tempfile.mkstemp()

    def tearDown(self):
        os.close(self.temp_fd)
        os.remove(self.temp_path)

    def run_test_case(self, input_str, expected_result):
        with open(self.temp_path, 'w') as temp_file:
            temp_file.write(input_str)

        result = execute_beer_preferences(self.temp_path)

        self.assertEqual(result, expected_result)

    def test_two_employees_which_like_different_beers(self):
        self.run_test_case("2 2\nYN NY", 2)

    def test_where_theres_extra_beer(self):
        self.run_test_case("6 3\nYNN YNY YNY NYY NYY NYN", 2)

    def test_where_theres_extra_beer_2(self):
        self.run_test_case("4 3\nYYN YYN YYN NNY", 2)

    def test_where_theres_four_employees_with_different_beer_preferences(self):
        self.run_test_case("4 4\nYNNN NYNN NNYN NNNY", 4)

    def test_where_theres_beer_no_one_likes(self):
        self.run_test_case("3 2\nYN YN YN", 1)

    def test_where_theres_no_beer(self):
        self.run_test_case("3 0\nYN YN YN", INVALID_NUM_OF_BEERS_MSG)

    def test_where_theres_no_employees(self):
        self.run_test_case("0 2\nYN YN YN", INVALID_NUM_OF_EMPLOYEES_MSG)

    def test_where_theres_too_many_employees(self):
        self.run_test_case("50 2\nYN YN YN", INVALID_NUM_OF_EMPLOYEES_MSG)

    def test_where_theres_too_many_beers(self):
        self.run_test_case("3 50\nYN YN YN", INVALID_NUM_OF_BEERS_MSG)

    def test_where_theres_employee_which_doesnt_like_beer(self):
        self.run_test_case("3 2\nYN NY NN", NO_BEER_PREFERENCE_MSG)

    def test_where_theres_invalid_preferences_line(self):
        self.run_test_case("3 2\nYN NY N", INVALID_PREFERENCES_LINE_MSG)

    def test_where_theres_invalid_preferences_line_2(self):
        self.run_test_case("3 2\nYN NY NNN", INVALID_PREFERENCES_LINE_MSG)

    def test_where_theres_invalid_preferences_line_3(self):
        self.run_test_case("3 2", INVALID_PREFERENCES_LINE_MSG)


if __name__ == '__main__':
    unittest.main()
