import time
import tracemalloc
from task4.src.task import find_ind 
import utils

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task4/textf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
k = int(f.readline())
b = list(map(int, f.readline().split()))
f.close()

inds = find_ind(a, b, n)

utils.write_file("task4/textf/output.txt", inds)

print('Тест примера')
utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()
