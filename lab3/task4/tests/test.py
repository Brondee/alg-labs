import time
import tracemalloc
from task4.src.task import count_interval 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('task4/textf/input.txt')

  res = count_interval(data)

  utils.write_file("task4/textf/output.txt", res)

  print('Тест примера')
  utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()