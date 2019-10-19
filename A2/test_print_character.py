from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import print_character
from unittest.mock import patch
import io


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_name(self, mock_stdout):
        name = {'Name': 'Nunu'}
        output = 'Name Nunu\n'
        print_character(name)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_race(self, mock_stdout):
        race = {'Race': 'human'}
        output = 'Race human\n'
        print_character(race)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_class(self, mock_stdout):
        self_class = {'Class': 'paladin'}
        output = 'Class paladin\n'
        print_character(self_class)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_health(self, mock_stdout):
        hp = {'HP': [1, 1]}
        output = 'HP: 1, 1\n'
        print_character(hp)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stren(self, mock_stdout):
        stren = {'Strength:': 14}
        output = 'Strength: 14\n'
        print_character(stren)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_dex(self, mock_stdout):
        dex = {'Dexterity:': 10}
        output = 'Dexterity: 10\n'
        print_character(dex)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_const(self, mock_stdout):
        constit = {'Constitution:': 11}
        output = 'Constitution: 11\n'
        print_character(constit)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_intel(self, mock_stdout):
        intel = {'Intelligence:': 9}
        output = 'Intelligence: 9\n'
        print_character(intel)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_wis(self, mock_stdout):
        wis = {'Wisdom:': 17}
        output = 'Wisdom: 17\n'
        print_character(wis)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_char(self, mock_stdout):
        char = {'Charisma:': 7}
        output = 'Charisma: 7\n'
        print_character(char)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_exp(self, mock_stdout):
        exp = {'Experience': 0}
        output = 'Experience 0\n'
        print_character(exp)
        self.assertEqual(mock_stdout.getvalue(), output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_inv(self, mock_stdout):
        inv = {'Inventory': ['Scale Armour of The Red-Dinosaur', "Zain's Crimson Falchion"]}
        output = "Inventory: Scale Armour of The Red-Dinosaur, Zain's Crimson Falchion\n"
        print_character(inv)
        self.assertEqual(mock_stdout.getvalue(), output)