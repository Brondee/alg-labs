import time
import tracemalloc
import unittest
from lab7.task2.src.task import min_operations 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_min_operations(self):
        # given
        data = utils.read_data('lab7/task2/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = min_operations(data[0])

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['14\n', '1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234'])
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()