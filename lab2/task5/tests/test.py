import time
import tracemalloc
from lab2.task5.src.task import has_majority 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()
    
  data = utils.read_data('lab2/task5/textf/input.txt')

  res = has_majority(data[1], data[0])

  utils.write_file("lab2/task5/textf/output.txt", res)

  print('Тест примера')
  utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

if __name__ == '__main__':
  example_test()