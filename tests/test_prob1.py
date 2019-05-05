import unittest

from daily_coding_prob1 import sum_exists

class TestSumExists(unittest.TestCase):
    def test_sum_exists(self):
        arr = [1,2,3,4]
        k = [7,10]
        for index,val in enumerate(k):
            result = sum_exists(arr, val)
            self.assertEquals(result,True if index%2 == 0 else False)

if __name__ == "__main__":
    unittest.main()
