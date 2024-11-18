import time
import tracemalloc
from lab2.task4.src.task import find_ind 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('lab2/task4/textf/input.txt')

  inds = find_ind(data[1], data[3], data[0])

  utils.write_file("lab2/task4/textf/output.txt", [inds])

  print('Тест примера')
  utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()