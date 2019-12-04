import unittest

from challenges.v_challenges import visits_on_circular_road
from challenges.m_challenges import max_zeros


class TestVisitsOnCircularRoad(unittest.TestCase):
    def test_1(self):
        n = 4
        visits_order = [1, 3, 2, 3, 1]
        result = visits_on_circular_road(n, visits_order)
        self.assertEqual(result, 6)

    def test_2(self):
        n = 3
        visits_order = [3]
        result = visits_on_circular_road(n, visits_order)
        self.assertEqual(result, 1)


class TestMaxZeros(unittest.TestCase):
    def test_1(self):
        n = 9
        result = max_zeros(n)
        self.assertEqual(result, 2)

    def test_2(self):
        n = 7
        result = max_zeros(n)
        self.assertEqual(result, 7)

    def test_2(self):
        n = 127
        result = max_zeros(n)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
