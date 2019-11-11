from unittest import TestCase
from A01166243_1510_assignments.A3.SUD import check_if_can_buy
from A01166243_1510_assignments.A3.constants import *
from unittest.mock import patch
import io


class TestCheckIfCanBuy(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_can_buy_1(self, mock_stdout):
        pick_item = 1
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 1000}
        expected_output = '\nYou have purchased Giorno Guccivana Handbag. Thank you for your purchase!\n'
        check_if_can_buy(STORE_PRICES, player, pick_item, STORE_LIST, [])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_can_buy_2(self, mock_stdout):
        pick_item = 2
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 1000}
        expected_output = '\nYou have purchased Alyx Rollercoaster Belt. Thank you for your purchase!\n'
        check_if_can_buy(STORE_PRICES, player, pick_item, STORE_LIST, [])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_can_buy_3(self, mock_stdout):
        pick_item = 3
        player = {'Name:': 'Attacker', 'Style Level:': [10, 10], 'Cash:': 1000}
        expected_output = '\nYou have purchased TRUE DAMAGE \'GIANTS\' Hoodie. Thank you for your purchase!\n'
        check_if_can_buy(STORE_PRICES, player, pick_item, STORE_LIST, [])
        self.assertEqual(mock_stdout.getvalue(), expected_output)