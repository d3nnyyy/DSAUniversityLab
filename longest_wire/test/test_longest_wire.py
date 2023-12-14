import unittest

from longest_wire.src.longest_wire import find_longest_wire


class TestFindLongestWire(unittest.TestCase):

    def test_equal_heights(self):
        result = find_longest_wire(2, [3, 3, 3])
        self.assertAlmostEqual(result, 5.65, delta=0.01)

    def test_single_height(self):
        result = find_longest_wire(100, [1, 1, 1, 1])
        self.assertEqual(result, 300.0)

    def test_variable_heights(self):
        result = find_longest_wire(4, [100, 2, 100, 2, 100])
        self.assertAlmostEqual(result, 396.32, delta=0.01)

    def test_complex_heights(self):
        result = find_longest_wire(4,
                                   [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66,
                                    28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93,
                                    34, 57, 51, 11, 39, 72])
        self.assertAlmostEqual(result, 2738.18, delta=0.01)


if __name__ == '__main__':
    unittest.main()
