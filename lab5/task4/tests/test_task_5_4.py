import time
import tracemalloc
import unittest
from lab5.task4.src.task import build_pyramid 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_build_pyramid(self):
        # given
        data = utils.read_data('lab5/task4/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = build_pyramid(data[0], data[1])

        utils.write_file("lab5/task4/textf/output.txt", res)

        print('Тест примера')
        utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, ['3\n', '1 4\n', '0 1\n', '1 3\n'])
        self.assertLess(time.perf_counter() - t_start, 2) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256) 

if __name__ == '__main__':
  unittest.main()