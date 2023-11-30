import unittest

from knuth_morris_pratt.src.knuth_morris_pratt import find_pattern_in_string


class TestFindPatternInString(unittest.TestCase):

    def test_pattern_found_at_beginning(self):
        result = find_pattern_in_string("abcdef", "abc")
        self.assertEqual(result, 0)

    def test_pattern_found_in_middle(self):
        result = find_pattern_in_string("abcdef", "cde")
        self.assertEqual(result, 2)

    def test_pattern_found_at_end(self):
        result = find_pattern_in_string("abcdef", "ef")
        self.assertEqual(result, 4)

    def test_pattern_not_found(self):
        result = find_pattern_in_string("abcdef", "xyz")
        self.assertEqual(result, -1)

    def test_empty_pattern(self):
        result = find_pattern_in_string("abcdef", "")
        self.assertEqual(result, 0)

    def test_empty_string_and_pattern(self):
        result = find_pattern_in_string("", "")
        self.assertEqual(result, 0)

    def test_repeated_pattern(self):
        result = find_pattern_in_string("ababab", "ab")
        self.assertEqual(result, 0)

    def test_long_pattern_found(self):
        result = find_pattern_in_string("abcabcabcabc", "abcabc")
        self.assertEqual(result, 0)

    def test_long_pattern_not_found(self):
        result = find_pattern_in_string("abcabcabcabc", "abcd")
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
