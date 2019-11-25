from unittest import TestCase
from A01166243_1510_assignments.A4.question_8 import digit_2_to_4


class TestDigit2To4(TestCase):
    def test_digit_2_to_4_digit_2(self):
        self.assertEqual(6, digit_2_to_4({0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}, [], 0, 0, 2))

    def test_digit_2_to_4_digit_3(self):
        self.assertEqual(6, digit_2_to_4({0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}, [], 0, 0, 5))

    def test_digit_2_to_4_digit_4(self):
        self.assertEqual(7, digit_2_to_4({0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}, [], 0, 0, 9))
