__author__ = 'Marcel'

import unittest
from calculator import calc


class TestCalculator(unittest.TestCase):
    def test_number(self):
        self.assertEqual(calc("5"), 5)

    def test_simple_expression(self):
        self.assertEqual(calc("1 PLUS 2"), 3)

    def test_complex_expression(self):
        self.assertEqual(calc("2 PLUS 5 MINUS 1 PLUS 4"), 10)


if __name__ == '__main__':
    unittest.main()
