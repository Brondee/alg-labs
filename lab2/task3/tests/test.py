import time
import tracemalloc
from task3.src.task import merge_sort
import utils

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task3/textf/input.txt')
n = int(f.readline())
arr_in = list(map(int, f.readline().split()))
f.close()

inversion_count = merge_sort(arr_in, 0, len(arr_in) - 1, 0)

utils.write_file("task3/textf/output.txt", [inversion_count])


print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
