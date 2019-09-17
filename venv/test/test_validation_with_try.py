import unittest
from unittest import mock
from input_validation import validation_with_try

class testCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

if __name__ == '__main__':
    unittest.main()