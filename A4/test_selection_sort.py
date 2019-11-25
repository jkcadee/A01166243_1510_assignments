from unittest import TestCase
from A01166243_1510_assignments.A4.question_4 import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort_5_items(self):
        a_list = [0, -1, 9, 30, 8]
        selection_sort(a_list)
        self.assertEqual([-1, 0, 8, 9, 30], a_list)

    def test_selection_sort_2_items(self):
        a_list = [0, -1]
        selection_sort(a_list)
        self.assertEqual([-1, 0], a_list)

    def test_selection_sort_invalid_items(self):
        with self.assertRaises(TypeError):
            selection_sort('a')
