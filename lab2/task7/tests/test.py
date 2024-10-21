import time
import tracemalloc
import random
from task7.src.task import max_subarray 
import utils

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task7/textf/input.txt')
n = int(f.readline())
arr_in = list(map(int, f.readline().split()))
f.close()

res = max_subarray(arr_in)

utils.write_file("task7/textf/output.txt", [res])

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()

# проверка по времени и памяти для худшего, среднего и лучшего случаев dwadwadaw
array_worst = sorted([random.randint(-1000, 1000) for _ in range(10000)], reverse=True)
array_middle = [random.randint(-1000, 1000) for _ in range(10000)]                      
array_best = sorted([random.randint(-1000, 1000) for _ in range(10000)])                
arrays = [array_worst, array_middle, array_best]
arr_names = ['Худший случай', "Средний случай", 'Лучший случай']

for i, arr in enumerate(arrays):
  t_start = time.perf_counter()
  tracemalloc.start()

  res = max_subarray(arr)
  print(arr_names[i])
  print('Время работы: %s секунд' % (time.perf_counter() - t_start))
  print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")

  tracemalloc.stop()

# PYTHONPATH=. python3 task7/tests/test.py