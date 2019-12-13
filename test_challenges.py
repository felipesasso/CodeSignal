import unittest

from challenges.l_challenges import last_digit_reg_exp
from challenges.v_challenges import visits_on_circular_road
from challenges.m_challenges import max_zeros, max_subarray
from challenges.n_challenges import number_of_operations
from challenges.s_challenges import square_digits_sequence

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

class TestMaxSubarray(unittest.TestCase):
    def test_1(self):
        input_array=[-1, 7, -2, 3, 4, 0, 1, -1]
        result = max_subarray(input_array)
        self.assertEqual(result, 13)

    def test_2(self):
        input_array=[-1, -2, -5, -1]
        result = max_subarray(input_array)
        self.assertEqual(result, 0)

class TestLastDigitRegExp(unittest.TestCase):
    def test_1(self):
        input_string="var_1__Int"
        result = last_digit_reg_exp(input_string)
        self.assertEqual(result, '1')

    def test_2(self):
        input_string="qq2q"
        result = last_digit_reg_exp(input_string)
        self.assertEqual(result, '2')

class TestNumberOfOperations(unittest.TestCase):

    def test_1(self):
        a = 432
        b = 72
        result = number_of_operations(a, b)
        self.assertEqual(result, 4)

    def test_2(self):
        a = 7
        b = 14
        result = number_of_operations(a, b)
        self.assertEqual(result, 1)

class TestSquareDigitsSequence(unittest.TestCase):
    def test_1(self):
        a0 = 16
        result = square_digits_sequence(a0)
        self.assertEqual(result, 9)

    def test_2(self):
        a0 = 612
        result = square_digits_sequence(a0)
        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()
