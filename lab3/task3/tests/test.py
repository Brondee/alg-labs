import time
import tracemalloc
from task3.src.task import pugalo_sort 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('task3/textf/input.txt')

  res = pugalo_sort(data[1], data[0][0], data[0][1])

  utils.write_file("task3/textf/output.txt", res)

  print('Тест примера')
  utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()