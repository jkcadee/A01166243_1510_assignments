from unittest import TestCase
from A01166243_1510_assignments.A2.dungeonsanddragons import choose_inventory
from unittest.mock import patch
import sys
import io


class TestChooseInventory(TestCase):
    def test_choose_inventory_print_(self):
        output = io.StringIO()
        sys.stout = output
        choose_inventory()


