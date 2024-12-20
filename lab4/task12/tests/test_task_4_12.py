import time
import tracemalloc
import unittest
from lab4.task12.src.task import recruits_line 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_recruits_line(self):
        # given
        data = utils.read_data('lab4/task12/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = recruits_line(data[0][0], data[1:])

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['2 3']) 
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)  

if __name__ == '__main__':
  unittest.main()