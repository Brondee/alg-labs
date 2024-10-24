import time
import tracemalloc
import random
from task1.src.task import merge_sort 
import utils

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
# f = open('task1/textf/input.txt')
# n = int(f.readline())
# arr_in = list(map(int, f.readline().split()))
# f.close()

data = utils.read_data('task1/textf/input.txt')

arr_sort = merge_sort(data[1], 0, len(data[1]) - 1)

utils.write_file("task1/textf/output.txt", arr_sort)

print('Тест примера')
utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()

# проверка по времени и памяти для худшего, среднего и лучшего случаев dwadwadaw
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
  utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))

  tracemalloc.stop()

# PYTHONPATH=. python3 task1/tests/test.py