from unittest import TestCase
from A01166243_1510_assignments.A4.question_8 import digit_1


class TestDigit1(TestCase):
    def test_digit_1(self):
        self.assertEqual(2, digit_1({0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 7: 4, 8: 7, 9: 6}, [], 0))
