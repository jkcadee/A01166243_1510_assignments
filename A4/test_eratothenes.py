from unittest import TestCase
from A01166243_1510_assignments.A4.question_1 import eratothenes
from unittest.mock import patch
import io


class TestEratothenes(TestCase):
    def test_eratothenes_1(self):
        self.assertEqual([], eratothenes(1))

    def test_eratothenes_10(self):
        self.assertEqual([2, 3, 5, 7], eratothenes(10))

    def test_eratothenes_30(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], eratothenes(30))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eratothenes_incorrect_input(self, mock_stdout):
        expected_output = "Wrong input!\n"
        eratothenes(-1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
