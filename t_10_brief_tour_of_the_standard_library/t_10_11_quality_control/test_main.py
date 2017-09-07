import unittest
from t_10_brief_tour_of_the_standard_library.t_10_11_quality_control import main


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(main.average([20, 30, 70]), 40.0)

    def test_average_round(self):
        self.assertEqual(round(main.average([1, 5, 7]), 1), 4.3)

    def test_average_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            main.average([])

    def test_average_type_error(self):
        with self.assertRaises(TypeError):
            main.average(20, 30, 70)

unittest.main()
