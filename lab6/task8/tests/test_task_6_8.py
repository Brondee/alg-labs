import time
import tracemalloc
import unittest
from lab6.task8.src.task import solve_hash 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_solve_hash(self):
        # given
        data = utils.read_data('lab6/task8/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = solve_hash(data)

        tracemalloc.stop()

        # then
        self.assertEqual(res, '3 1 1')
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()