import time
import tracemalloc
import unittest
from lab4.task6.src.task import queue_func_min 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_queue_func_min(self):
        # given
        data = utils.read_data('lab4/task6/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = queue_func_min(data[1:])

        utils.write_file("lab4/task6/textf/output.txt", res)

        print('Тест примера')
        utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, ['1\n', '1\n', '10\n'])
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
  unittest.main()