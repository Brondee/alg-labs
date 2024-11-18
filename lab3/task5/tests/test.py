import time
import tracemalloc
import unittest
from lab3.task5.src.task import hirsh_index 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_hirsh_index(self):
        # given
        data = utils.read_data('lab3/task5/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = hirsh_index(data[0])

        utils.write_file("lab3/task5/textf/output.txt", res)

        print('Тест примера')
        utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, 3) 
        self.assertLess(time.perf_counter() - t_start, 5) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256) 

if __name__ == '__main__':
  unittest.main()