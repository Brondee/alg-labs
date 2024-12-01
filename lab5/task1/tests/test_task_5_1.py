import time
import tracemalloc
import unittest
from lab5.task1.src.task import is_heap 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_is_heap(self):
        # given
        data = utils.read_data('lab5/task1/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = is_heap(data[0], data[1])

        tracemalloc.stop()

        # then
        self.assertEqual(res, 'YES')
        self.assertLess(time.perf_counter() - t_start, 2) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256) 

if __name__ == '__main__':
  unittest.main()