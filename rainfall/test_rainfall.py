import unittest
from rainfall import *

class RainfallTests(unittest.TestCase):

    def test_basic_1(self):
        measurements = [1.0, 2.0, 1.5, 2.5, 99999.0]
        self.assertEqual(rainfall(measurements), 1.75)

    def test_basic_2(self):
        measurements = [10.5, 15.489, 1.0, 3.154, 22.0, 99999.0]
        self.assertEqual(rainfall(measurements), 10.4286)

    def test_all_zeroes(self):
        measurements = [0.0, 0.0, 0.0, 0.0, 99999.0]
        self.assertEqual(rainfall(measurements), 0.0)

    def test_has_zeroes(self):
        measurements = [2.0, 0.0, 1.0, 0.0, 99999.0]
        self.assertEqual(rainfall(measurements), 1.5)

    def test_after_sentinel(self):
        measurements = [0.0, 1.0, 3.0, 0.0, 99999.0, 13.0, 145.0]
        self.assertEqual(rainfall(measurements), 2.0)

    def test_no_data(self):
        measurements = [99999.0, 13.0, 145.0]
        self.assertEqual(rainfall(measurements), 0.0)

    def test_with_negatives(self):
        measurements = [2.0, -1.0, 3.0, -3.0, 0.0, 99999.0]
        self.assertEqual(rainfall(measurements), 2.5)

    def test_all_negatives(self):
        measurements = [-1.0, -1.0, -3.0, 99999.0]
        self.assertEqual(rainfall(measurements), 0.0)

    def test_long(self):
        measurements = [4, 7, -1.4, 19, -1, 20, 0, 0, 0, -41.1, 13, 14, 11, 8,
                2, 18, 16, -4., 6, -123, -15, -0.01, 0, 12, 5, 0, 0, 0, 0, 10,
                3, 9, 17, 15, 1, 99999, 5, 4, 8749, 5138, 3548, 127, 0]
        self.assertEqual(rainfall(measurements), 10.5)


if __name__ == '__main__':
    unittest.main()
