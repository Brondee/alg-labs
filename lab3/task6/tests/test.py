import time
import tracemalloc
from task6.src.task import sum_of_tenth 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('task6/textf/input.txt')

  res = sum_of_tenth(data[1], data[2])

  utils.write_file("task6/textf/output.txt", [res])

  print('Тест примера')
  utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()