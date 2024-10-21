import time
import tracemalloc
from task8.src.task import multiply_polynomials 
import utils

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task8/textf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
b = list(map(int, f.readline().split()))
f.close()

inversion_count = multiply_polynomials(a, b, n)

utils.write_file("task8/textf/output.txt", [inversion_count])

print('Тест примера')
utils.end_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
tracemalloc.stop()
