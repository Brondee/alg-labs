import time
import tracemalloc
from task5.src.task import has_majority 

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task5/textf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
f.close()

res = has_majority(a, n)

f2 = open("task5/textf/output.txt", 'w')
f2.write(str(res))
f2.close()

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
