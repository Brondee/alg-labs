import time
import tracemalloc
import unittest
from lab7.task4.src.task import longest_common_subsequence 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_longest_common_subsequence(self):
        # given
        data = utils.read_data('lab7/task4/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = longest_common_subsequence(data[1], data[3])

        tracemalloc.stop()

        # then
        self.assertEqual(res, 2)
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()