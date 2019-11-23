from unittest import TestCase
from A01166243_1510_assignments.A4.question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            gcd(0, 0)

    def test_gcd_1(self):
        self.assertEqual(1, gcd(70, 9))

    def test_gcd_10(self):
        self.assertEqual(10, gcd(50, 30))
        