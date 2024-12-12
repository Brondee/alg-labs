import time
import tracemalloc
import unittest
from lab7.task1.src.task import min_coins 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_min_coins(self):
        # given
        data = utils.read_data('lab7/task1/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = min_coins(data[0][0], data[1])

        tracemalloc.stop()

        # then
        self.assertEqual(res, 9)
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()