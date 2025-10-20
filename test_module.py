import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):

    def setUp(self):
        # Test data
        self.data = [0,1,2,3,4,5,6,7,8]
        self.result = calculate(self.data)

    def test_mean(self):
        expected_axis0 = [3.0, 4.0, 5.0]
        expected_axis1 = [1.0, 4.0, 7.0]
        expected_flattened = 4.0
        self.assertEqual(self.result['mean'][0], expected_axis0)
        self.assertEqual(self.result['mean'][1], expected_axis1)
        self.assertAlmostEqual(self.result['mean'][2], expected_flattened)

    def test_variance(self):
        expected_axis0 = [6.0, 6.0, 6.0]
        expected_axis1 = [0.6666666666666666, 0.6666666666666666, 0.6666666666666666]
        expected_flattened = 6.666666666666667
        self.assertEqual(self.result['variance'][0], expected_axis0)
        self.assertEqual(self.result['variance'][1], expected_axis1)
        self.assertAlmostEqual(self.result['variance'][2], expected_flattened)

    def test_std(self):
        expected_axis0 = [2.449489742783178, 2.449489742783178, 2.449489742783178]
        expected_axis1 = [0.816496580927726, 0.816496580927726, 0.816496580927726]
        expected_flattened = 2.581988897471611
        self.assertEqual(self.result['standard deviation'][0], expected_axis0)
        self.assertEqual(self.result['standard deviation'][1], expected_axis1)
        self.assertAlmostEqual(self.result['standard deviation'][2], expected_flattened)

    def test_max(self):
        expected_axis0 = [6, 7, 8]
        expected_axis1 = [2, 5, 8]
        expected_flattened = 8
        self.assertEqual(self.result['max'][0], expected_axis0)
        self.assertEqual(self.result['max'][1], expected_axis1)
        self.assertEqual(self.result['max'][2], expected_flattened)

    def test_min(self):
        expected_axis0 = [0, 1, 2]
        expected_axis1 = [0, 3, 6]
        expected_flattened = 0
        self.assertEqual(self.result['min'][0], expected_axis0)
        self.assertEqual(self.result['min'][1], expected_axis1)
        self.assertEqual(self.result['min'][2], expected_flattened)

    def test_sum(self):
        expected_axis0 = [9, 12, 15]
        expected_axis1 = [3, 12, 21]
        expected_flattened = 36
        self.assertEqual(self.result['sum'][0], expected_axis0)
        self.assertEqual(self.result['sum'][1], expected_axis1)
        self.assertEqual(self.result['sum'][2], expected_flattened)

    def test_invalid_input(self):
        # Less than 9 numbers should raise ValueError
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
