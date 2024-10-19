import time
import tracemalloc
from task4.src.task import find_ind 

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

f2 = open("task4/textf/output.txt", 'w')
f2.write((" ").join(list(map(str, inds))))
f2.close()

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
