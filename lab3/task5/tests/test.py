import time
import tracemalloc
from task5.src.task import hirsh_index 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('task5/textf/input.txt')

  res = hirsh_index(data[0])

  utils.write_file("task5/textf/output.txt", [res])

  print('Тест примера')
  utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()