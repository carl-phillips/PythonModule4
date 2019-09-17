import unittest
from unittest import mock
from input_validation import validation_with_try

class testCase(unittest.TestCase):
    def test_average_negative_input_1(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

    def test_average_negative_input_2(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)

    def test_average_negative_input_3(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, 98, -78)

if __name__ == '__main__':
    unittest.main()
