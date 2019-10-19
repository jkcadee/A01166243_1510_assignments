from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import choose_inventory
from unittest.mock import patch


class TestChooseInventory(TestCase):
    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, -1])
    def test_choose_inventory_get_item(self, mock_input):
        item_to_get = choose_inventory()
        output = ["Mango's Smashing Steel-Toed Boots",
                  "The Swedish Sniper Longbow",
                  "Crown of the Mews",
                  "Engraved APEX: MMXV Cloak",
                  "The Bottomless Hungrypouch",
                  "Plup's Sensational Pulper",
                  "Zain's Crimson Falchion",
                  "Lightning's Summit Axe",
                  "The Godslayer's Tome",
                  "Cody's Convenient ice Blasting Dragon Wand",
                  "Scale Armour of The Red-Sun",
                  "Wizzy's Excellent Falcon-Grade Kneepads",
                  "20XX-Calibrated Shinegoggles",
                  "The Inseparable 'Pew' and 'Fat' Daggers",
                  "Johnny's Flaming Falcon-Grade Gloves",
                  "Staff of Eternal Melee"]
        self.assertEqual(output, item_to_get)

    @patch('builtins.input', side_effect=[-1])
    def test_choose_inventory_just_exit(self, mock_input):
        item_to_get = choose_inventory()
        output = []
        self.assertEqual(output, item_to_get)

    @patch('builtins.input', side_effect=[0, -1])
    def test_choose_inventory_no_item(self, mock_input):
        item_to_get = choose_inventory()
        output = []
        self.assertEqual(output, item_to_get)

    @patch('builtins.input', side_effect=[-6, -1])
    def test_choose_inventory_wrong_choice(self, mock_input):
        item_to_get = choose_inventory()
        output = []
        self.assertEqual(output, item_to_get)
