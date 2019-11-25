from unittest import TestCase
from A01166243_1510_assignments.A4.question_3 import dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra_dutch(self):
        dutch = ['red', 'white', 'blue', 'red', 'blue', 'white', 'blue', 'red', 'white']
        dijkstra(dutch)
        self.assertEqual(['red', 'red', 'red', 'white', 'white', 'white', 'blue', 'blue', 'blue'], dutch)

    def test_dijkstra_dutch_two(self):
        dutch = ['red', 'blue', 'white', 'blue', 'red', 'white']
        dijkstra(dutch)
        self.assertEqual(['red', 'red', 'white', 'white', 'blue', 'blue'], dutch)

    def test_dijkstra_dutch_one(self):
        dutch = ['red', 'blue', 'white']
        dijkstra(dutch)
        self.assertEqual(['red', 'white', 'blue'], dutch)
