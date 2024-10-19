import time
import tracemalloc
from task8.src.task import multiply_polynomials 

# проверка по времени и памяти для примера
tracemalloc.start()
t_start = time.perf_counter()
  
f = open('task8/textf/input.txt')
n = int(f.readline())
a = list(map(int, f.readline().split()))
b = list(map(int, f.readline().split()))
f.close()

inversion_count = multiply_polynomials(a, b, n)

f2 = open("task8/textf/output.txt", 'w')
f2.write((" ").join(list(map(str, inversion_count))))
f2.close()

print('Тест примера')
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()
