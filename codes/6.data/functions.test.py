import unittest
import functions as func


class FunctionsTest(unittest.TestCase):
    def test_get_data(self):
        reds, blues, red_blues = func.get_data('./history.csv')
        self.assertEqual(len(reds), 2229)
        self.assertEqual(len(blues), 2229)
        self.assertEqual(len(red_blues), 2229)
        self.assertEqual(len(reds[0]), 5)
        self.assertEqual(len(blues[0]), 2)
        self.assertEqual(len(red_blues[0]), 7)

    def test_get_sum_avg_diff(self):
        source = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        avg_total = 90
        sums, avgs, diffs = func.get_sum_avg_diff(source, avg_total)
        self.assertEqual(sums, [15, 40])
        self.assertEqual(avgs, [90, 90])
        self.assertEqual(diffs, [75, 50])

    def test_get_diff_count(self):
        diffs = [11, 21, 31, 41, 51]
        diff_count = func.get_diff_count(diffs)
        self.assertEqual(diff_count,
                         {'0-10': 0, '10-20': 1, '20-30': 1, '30-40': 1, '40-50': 1, '50-60': 1, })

    def test_get_reds_3area(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        dic_case = func.get_reds_3area(reds)
        self.assertEqual(dic_case,
                         {'2-2-1': 1, '5-0-0': 1, '0-0-5': 1})

    def test_get_reds_4area(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        dic_case = func.get_reds_4area(reds)
        self.assertEqual(dic_case,
                         {'1-1-1-2': 1, '3-2-0-0': 1, '0-0-3-2': 1})

    def test_get_reds_5area(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        dic_case = func.get_reds_5area(reds)
        self.assertEqual(
            dic_case, {'1-1-1-1-1': 1, '5-0-0-0-0': 1, '0-0-0-0-5': 1})

    def test_area5_filter(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        result = func.area5_filter(reds)
        self.assertEqual(result, [[7, 11, 19, 24, 30]])

    def test_get_ac_count(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        ac_count = func.get_ac_count(reds, 5)
        self.assertEqual(ac_count, {6: 1, 0: 2})

    def test_get_prime_stats(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        prime_count, prime_stats = func.get_prime_stats(reds)
        self.assertEqual(prime_count, [3, 3, 1])
        self.assertEqual(prime_stats, {0: 0, 1: 1, 2: 0, 3: 2, 4: 0, 5: 0})

    def test_get_hot(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        hots = func.get_hot(reds)
        self.assertEqual(hots, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0, 11: 1, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0,
                         18: 0, 19: 1, 20: 0, 21: 0, 22: 0, 23: 0, 24: 1, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1})

    def test_get_all_5degrees(self):
        prefers = [1, 2, 3, 4, 5, 6]
        results = func.get_all_5degrees(prefers)
        self.assertEqual(results, [(1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (
            1, 2, 3, 5, 6), (1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6)])

    def test_sum_filter(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        result = func.sum_filter(reds)
        self.assertEqual(result, [[7, 11, 19, 24, 30]])

    def test_area3_filter(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        result = func.area3_filter(reds)
        self.assertEqual(result, [[7, 11, 19, 24, 30]])

    def test_area4_filter(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        result = func.area4_filter(reds)
        self.assertEqual(result, [[7, 11, 19, 24, 30]])

    def test_ac_filter(self):
        reds = [[7, 11, 19, 24, 30], [1, 2, 3, 4, 5], [35, 34, 33, 32, 31]]
        result = func.ac_filter(reds)
        self.assertEqual(result, [[7, 11, 19, 24, 30]])


if __name__ == '__main__':
    unittest.main()
