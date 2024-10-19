import time
import tracemalloc
import random
from task1.src.task import merge_sort 

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task1/textf/input.txt')
n = int(f.readline())
arr_in = list(map(int, f.readline().split()))
f.close()

arr_sort = merge_sort(arr_in, 0, len(arr_in) - 1)

f2 = open("task1/textf/output.txt", 'w')
f2.write((" ").join(list(map(str, arr_sort))))
f2.close()

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
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
  print('Время работы: %s секунд' % (time.perf_counter() - t_start))
  print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")

  tracemalloc.stop()

# PYTHONPATH=. python3 task1/tests/test.py