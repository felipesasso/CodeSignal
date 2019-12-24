import unittest

from company_challenges.Uber.main import fareEstimator, fancyRide


class TestUberChallenges(unittest.TestCase):
    def test_fare_estimator_1(self):
        ride_time = 30
        ride_distance = 7
        cost_per_minute = [0.2, 0.35, 0.4, 0.45]
        cost_per_mile = [1.1, 1.8, 2.3, 3.5]
        result = fareEstimator(
            ride_time, ride_distance, cost_per_minute, cost_per_mile
        )
        self.assertEqual(result, [13.7, 23.1, 28.1, 38])

    def test_fare_estimator_2(self):
        ride_time = 15
        ride_distance = 9
        cost_per_minute = [0.2, 0.34, 0.35, 0.45, 1]
        cost_per_mile = [1.1, 1.8, 1.9, 1.7, 5]
        result = fareEstimator(
            ride_time, ride_distance, cost_per_minute, cost_per_mile
        )
        self.assertEqual(result, [12.9, 21.3, 22.35, 22.05, 60])

    def test_fancy_ride_1(self):
        l= 30
        fares= [0.3, 0.5, 0.7, 1, 1.3]
        result = fancyRide(l, fares)
        self.assertEqual(result, 'UberXL')

    def test_fancy_ride_2(self):
        l= 15
        fares= [0.7, 1, 1.3, 1.5, 1.7]
        result = fancyRide(l, fares)
        self.assertEqual(result, 'UberPlus')

if __name__ == "__main__":
    unittest.main()
