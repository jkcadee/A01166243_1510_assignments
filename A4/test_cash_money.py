from unittest import TestCase
from A01166243_1510_assignments.A4.question_5 import cash_money


class TestCashMoney(TestCase):
    def test_cash_money_all_filled(self):
        self.assertEqual({100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1},
                         cash_money(188.41))

    def test_cash_money_one_filled_cents(self):
        self.assertEqual({100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 1},
                         cash_money(0.01))

    def test_cash_money_one_filled_dollars(self):
        self.assertEqual({100: 0, 50: 0, 20: 0, 10: 0, 5: 1, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0},
                         cash_money(5.00))

    def test_cash_money_invalid_input(self):
        with self.assertRaises(ValueError):
            cash_money(-1.0)