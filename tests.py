import unittest
import random
import statistics
from node import Node, add_rand
from calculations import Calculations

class TestNode(unittest.TestCase):

    def test_init_int(self):
        self.assertEqual(Node(2).value, 2)

    def test_init_double(self):
        self.assertEqual(Node(2.8).value, 2)

    def test_init_char(self):
        self.assertRaises(ValueError, Node, 'a')

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.nodes = []
        for i in range(10):
            self.nodes.append(Node(random.randint(0, 20)))
        
        self.root = self.nodes[0]

        x = 1
        while x < 10:
            add_rand(self.root, self.nodes[x])
            x += 1

        self.calc = Calculations(self.root)

    def test_calculate_sum_root(self):
        self.assertEqual(self.calc.calculate_sum(self.root), sum(n.value for n in self.nodes))
        self.assertEqual(self.calc.count, len(self.nodes))

        x = sorted(self.calc.nodes, key=lambda x: x.value)
        y = sorted(self.nodes, key=lambda x: x.value)

        for i in range(len(x)):
            self.assertEqual(x[i].value, y[i].value)

    def test_calculate_average(self):
        self.assertEqual(self.calc.calculate_average(), sum(n.value for n in self.nodes) / len(self.nodes))

    def test_calculate_median(self):
        statistics.median(n.value for n in self.nodes)
        


if __name__ == '__main__':
    unittest.main()