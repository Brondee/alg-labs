import time
import tracemalloc
import unittest
from lab6.task6.src.task import process_fibonacci 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_process_fibonacci(self):
        # given
        data = utils.read_data('lab6/task6/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = process_fibonacci(data[1:])

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['Yes\n', 'Yes\n', 'Yes\n', 'No\n', 'Yes\n', 'No\n', 'No\n', 'Yes\n'])
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()