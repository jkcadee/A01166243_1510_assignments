from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import get_health
from unittest.mock import patch
import io


class TestGetHealth(TestCase):
    @patch('random.randint', return_value=6)
    def test_get_health(self, mock_random):
        actual_class = get_health('barbarian')
        expected_health = 6
        self.assertEqual(actual_class, expected_health)

    @patch('random.randint', return_value=6)
    def test_get_health_2(self, mock_random):
        actual_class = get_health('wizard')
        expected_health = 6
        self.assertEqual(actual_class, expected_health)

    @patch('random.randint', return_value=1)
    def test_get_health_3(self, mock_random):
        actual_class = get_health('rogue')
        expected_health = 1
        self.assertEqual(actual_class, expected_health)
