import time
import tracemalloc
import unittest
from lab4.task8.src.task import postfix 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_postfix(self):
        # given
        data = utils.read_data('lab4/task8/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = postfix(data[1])

        tracemalloc.stop()

        # then
        self.assertEqual(res, -102)
        self.assertLess(time.perf_counter() - t_start, 2)  
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)  

if __name__ == '__main__':
  unittest.main()