import time
import tracemalloc
import random
from lab2.task1.src.task import merge_sort 
import utils

def example_test():
  # проверка по времени и памяти для примера
  tracemalloc.start()
  t_start = time.perf_counter()

  data = utils.read_data('lab2/task1/textf/input.txt')

  arr_sort = merge_sort(data[1], 0, len(data[1]) - 1)

  utils.write_file("lab2/task1/textf/output.txt", [arr_sort])

  print('Тест примера')
  utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
  tracemalloc.stop()

def cases_test():
  # проверка по времени и памяти для худшего, среднего и лучшего случаев
  array_worst = sorted([random.randint(1, 1000) for _ in range(10000)], reverse=True)
  array_middle = [random.randint(1, 1000) for _ in range(10000)]                      
  array_best = sorted([random.randint(1, 1000) for _ in range(10000)])                
  arrays = [array_worst, array_middle, array_best]
  arr_names = ['Худший случай', "Средний случай", 'Лучший случай']

  for i, arr in enumerate(arrays):
    t_start = time.perf_counter()
    tracemalloc.start()

    arr_sort = merge_sort(arr, 0, len(arr) - 1)
    print(arr_names[i])
    utils.print_end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))

    tracemalloc.stop()

if __name__ == '__main__':
  example_test()
  cases_test()