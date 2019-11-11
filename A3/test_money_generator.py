from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import money_generator
from unittest.mock import patch


class TestMoneyGenerator(TestCase):
    @patch('random.randint', return_value=1)
    def test_money_generator_1_luck(self, mock_random):
        self.assertEqual(100, money_generator())

    @patch('random.randint', return_value=2)
    def test_money_generator_2_luck(self, mock_random):
        self.assertEqual(200, money_generator())

