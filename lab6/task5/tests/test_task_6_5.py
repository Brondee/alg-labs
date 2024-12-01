import time
import tracemalloc
import unittest
from lab6.task5.src.task import process_elections 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_process_elections(self):
        # given
        data = utils.read_data('lab6/task5/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = process_elections(data)

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['ivanov 900\n', 'petr 70\n', 'tourist 3\n'])
        self.assertLess(time.perf_counter() - t_start, 6) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512) 

if __name__ == '__main__':
  unittest.main()