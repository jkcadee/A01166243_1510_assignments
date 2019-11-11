from unittest import TestCase
from A01166243_1510_assignments.A3.character import print_character
from unittest.mock import patch
import io


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_name(self, mock_stdout):
        name = {'Name:': 'Nunu'}
        output = 'Name: Nunu\n'
        print_character(name)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_SL(self, mock_stdout):
        health = {'Style Level:': [10, 10]}
        output = 'Style Level: 10, 10\n'
        print_character(health)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_inventory(self, mock_stdout):
        inventory = {'Inventory:': []}
        output = 'Inventory: \n'
        print_character(inventory)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_cash(self, mock_stdout):
        cash = {'Cash:': 1000}
        output = 'Cash: 1000\n'
        print_character(cash)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_position(self, mock_stdout):
        position = {'Position:': [1, 1]}
        output = 'Position: 1, 1\n'
        print_character(position)
        self.assertEqual(mock_stdout.getvalue(), output)