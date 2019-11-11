from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import shopping
from A01166243_1510_assignments.A3.constants import *
from unittest.mock import patch


class TestShopping(TestCase):
    @patch('builtins.input', side_effect=[-1])
    def test_choose_inventory_just_exit(self, mock_input):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 0], 'Cash:': 0}
        item_to_get = shopping(STORE_LIST, player, STORE_PRICES)
        output = []
        self.assertEqual(output, item_to_get)

    @patch('builtins.input', side_effect=[0, -1])
    def test_choose_inventory_no_item(self, mock_input):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 0], 'Cash:': 0}
        item_to_get = shopping(STORE_LIST, player, STORE_PRICES)
        output = []
        self.assertEqual(output, item_to_get)

    @patch('builtins.input', side_effect=[-6, -1])
    def test_choose_inventory_wrong_choice(self, mock_input):
        player = {'Name:': 'Attacker', 'Style Level:': [10, 0], 'Cash:': 0}
        item_to_get = shopping(STORE_LIST, player, STORE_PRICES)
        output = []
        self.assertEqual(output, item_to_get)

