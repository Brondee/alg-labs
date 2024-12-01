import time
import tracemalloc
import unittest
from lab5.task3.src.task import network_packets 
import utils

class AlgorithmsSortTestCase(unittest.TestCase):

    def test_should_check_success_of_network_packets(self):
        # given
        data = utils.read_data('lab5/task3/textf/input.txt')

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = network_packets(data[0][0], data[1:])

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['0', '3', '10'])
        self.assertLess(time.perf_counter() - t_start, 2) 
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256) 

if __name__ == '__main__':
  unittest.main()