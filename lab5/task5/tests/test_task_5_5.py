import time
import tracemalloc
import unittest
from lab5.task5.src.task import task_manager 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_task_manager(self):
        # given
        data = utils.read_data('lab5/task5/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = task_manager(data[0][0], data[0][1], data[1])

        utils.write_file("lab5/task5/textf/output.txt", res)

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['0 0\n', '1 0\n', '0 1\n', '1 2\n', '0 4\n'])
        self.assertLess(time.perf_counter() - t_start, 2) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256) 

if __name__ == '__main__':
  unittest.main()